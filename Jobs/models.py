from django.db import models

from django.contrib.auth.models import User

    
class Jobs(models.Model):
    
    description = models.CharField(max_length=2000)
    company_name = models.CharField(max_length=100)
    experience = models.IntegerField()
    job_id = models.CharField(max_length=100)
    job_url = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    skills_required = models.CharField(max_length=1000)
    publishing_time = models.DateTimeField(auto_now=True)
    last_date_of_application = models.DateField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
# Create your models here.
