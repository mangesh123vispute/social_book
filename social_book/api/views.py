
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
from .forms import UserLoginForm
from django.contrib import messages
from .forms import UploadFileForm
from .models import UploadedFile
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

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
                login(request, user)
                messages.success(request, "You have successfully logged in!")
                return redirect('/')  
            else:
                messages.error(request, "Invalid credentials. Please try again.")
        else:
            messages.error(request, "Invalid credentials. Please try again.")
    else:
        form = UserLoginForm()
        
    return render(request, 'user/login.html', {'form': form})



def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
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
