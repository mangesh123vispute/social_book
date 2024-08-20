import pyotp # type: ignore
from datetime import datetime,timedelta
from django.conf import settings
from django.core.mail import send_mail
def send_otp(request,user):
    totp=pyotp.TOTP(pyotp.random_base32(), interval=60)
    otp=totp.now()
    request.session['otp_secret_key']=totp.secret
    valid_date=datetime.now()+timedelta(minutes=1)
    request.session['otp_valid_date']=str(valid_date)

     # Email details
    subject = 'Your OTP Code'
    message = f'Your one-time password (OTP) is {otp}. It will expire in one minute.'
    from_email = settings.EMAIL_HOST_USER  
    to_email = user.email

      # Send email
    try:
        send_mail(subject, message, from_email, [to_email])
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

    print(f"Your one time password is {otp}")
