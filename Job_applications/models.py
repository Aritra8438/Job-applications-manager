from django.db import models
from Users.models import User


class Job_application(models.Model):
    job_url = models.TextField(max_length=100)
    next_event_date = models.TimeField(auto_now_add=True)

    class Status(models.TextChoices):
        APPLIED = "Applied"
        UNDER_CONSIDERATION = "Under Consideration"
        INTERVIEW = "Interview"
        DECLINED = "Declined"
        ACCEPTED = "Accepted"

    status = models.CharField(
        max_length=30, choices=Status.choices, default=Status.APPLIED
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
