from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Job_application
from django.utils import timezone


def send_email():
    subject = "About your interviews"

    interviews = Job_application.objects.filter(status="Interview")
    for interview in interviews:
        if interview.user is None:
            return
        user_email = interview.user.email
        date_of_jobevent = interview.next_event_date
        # res = send_mail(
        #     subject,
        #     "Hello",
        #     settings.EMAIL_HOST_USER,
        #     [user_email],
        #     fail_silently=False,
        # )
        # Needs to b implemented
