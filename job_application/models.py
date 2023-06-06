from django.db import models
from Jobs.models import Jobs
from Users.models import User


class job_applications(models.Model):
    id = models.IntegerField(primary_key=True)
    job_url = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    time = models.TimeField(auto_now_add=True)

    class Status(models.TextChoices):
        APPLIED = "Applied"
        UNDER_CONSIDERATION = "Under Consideration"
        INTERVIEW = "Interview"
        DECLINED = "Declined"
        ACCEPTED = "Accepted"

    status = models.CharField(
        max_length=30, choices=Status.choices, default=Status.APPLIED
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
