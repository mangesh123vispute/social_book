
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
from .forms import UserLoginForm
from django.contrib import messages
from .forms import UploadFileForm
from .models import UploadedFile
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .utils import send_otp
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
import pyotp  # type: ignore


User=get_user_model()


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                new_user = form.save(commit=False)
                new_user.set_password(form.cleaned_data['password'])
                new_user.save()
                
                user = authenticate(username=new_user.username, password=form.cleaned_data['password'])
                login(request, user)
                messages.success(request, 'You have successfully registered!')
                return redirect('/')
            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
                return render(request, 'user/register.html', {'form': form})
        else:
            # Adding form errors to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return render(request, 'user/register.html', {'form': form})
    else:
        form = UserRegistrationForm()
    return render(request, 'user/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:    
                send_otp(request,user)
                request.session['username'] = username
                messages.success(request, "OTP has been sent to your email.")
                return redirect('otp')  
            else:
                messages.error(request, "Invalid credentials. Please try again.")
        else:
            messages.error(request, "Invalid credentials. Please try again.")
    else:
        form = UserLoginForm()
        
    return render(request, 'user/login.html', {'form': form})

def otp_view(request):
    if request.method == 'POST':
        print('I am getting called',request.POST)
        otp = request.POST['otp']
        username=request.session['username']
        otp_secret_key=request.session['otp_secret_key']
        otp_valid_until=request.session['otp_valid_date']

        if otp_secret_key and otp_valid_until is not None:
            valid_until=datetime.fromisoformat(otp_valid_until)
            if valid_until > datetime.now():
                totp = pyotp.TOTP(otp_secret_key, interval=60)
                if totp.verify(otp):
                    user = get_object_or_404(User, username=username)
                    login(request, user)
                    print("Login successful!")

                     # Send email notification
                    subject = 'Login Successful'
                    message = 'You have successfully logged in to your account.'
                    from_email = settings.EMAIL_HOST_USER
                    to_email = user.email

                    try:
                        send_mail(subject, message, from_email, [to_email])
                        print("Login notification email sent successfully!")
                    except Exception as e:
                        print(f"Failed to send email: {e}")

                    # Clean up session data
                    del request.session['otp_secret_key']
                    del request.session['otp_valid_date']
                    messages.success(request, "Login successful!")
                    return redirect('/')
                else:
                    messages.error(request, "Invalid OTP. Please try again.")
            else:
                messages.error(request, "OTP expired. Please try again.")
        else:
            messages.error(request, "Opps, something went wrong. Please try again.")

    return render(request, 'user/otp.html',{})


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have successfully logged out!')
    return redirect('/')
 
    

def authors_sellers(request):
    authors_sellers=User.objects.filter(public_visibility=True)
    return render(request, 'pages/Authors&Sellers.html',{'authors_sellers':authors_sellers})


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)  
            uploaded_file.user = request.user 
            uploaded_file.save()  
            return redirect('/api/upload')
    else:
        form = UploadFileForm()
    return render(request, 'pages/upload_file.html', {'form': form})

def uploaded_files(request):
    files = UploadedFile.objects.all()
    return render(request, 'pages/uploaded_files.html', {'files': files})

@login_required
def user_profile(request):
    books=UploadedFile.objects.filter(user=request.user)
    return render(request, 'user/profile.html',{'books':books})