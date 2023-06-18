from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Job_application 
from django.utils import timezone

def send_email():
    subject = 'Hey. This is your job management platform'
    message = 'Last date to apply '
    
    interviews = Job_application.objects.filter(status = 'Interview')
    for interview in interviews: 
        
        user_email = interview.user.email
        date_of_jobevent = interview.next_event_date
        jobName = 'job'
        
        if(date_of_jobevent) :
            num_days = date_of_jobevent - timezone.now().date()
            message = 'Hey. This is your job management platform. Your interview for {} is in {} days'.format(jobName, num_days)
        
        if(num_days and num_days>0 and num_days<=1):                
            res= send_mail(subject,           
            message, settings.EMAIL_HOST_USER, [user_email], fail_silently=False)
            if(res ):            
                print('Success!')            
        