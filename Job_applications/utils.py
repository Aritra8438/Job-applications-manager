from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Job_application 
from django.utils import timezone

def send_email(email):
    subject = 'Hey. This is your job management platform'
    message = 'Last date to apply '
    
    interviews = Job_application.objects.filter(status = 'Interview')
    for interview in interviews: 
        
        user_email = interview.user.email
        date_of_jobevent = interview.eventdate
        jobName = 'job'
        if(interview.job_name) :
            jobName = interview.job_name
        print(date_of_jobevent)
        if(date_of_jobevent) :
            num_days = date_of_jobevent - timezone.now().date()
            print(num_days)
            message = 'Hey. This is your job management platform. Your interview for {} is in {} days'.format(jobName, num_days)
        else :
            message = 'Hey. This is your job management platform. Your interview for {} is approaching'.format(jobName)   
                        
        res= send_mail(subject,           
        message, settings.EMAIL_HOST_USER, [user_email], fail_silently=False)
        if(res ):            
            print('Success!')            
        