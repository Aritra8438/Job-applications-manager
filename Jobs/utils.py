from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings

def send_email(request,email):
    subject = 'Hey. This is your job management platform'
    message = 'Last date to apply '
                    
    res= send_mail(subject,           
    message, settings.EMAIL_HOST_USER, [email], fail_silently=False)
    if(res ):            
        print('Success!')            
    messages.success(request, 'Success!')                                    