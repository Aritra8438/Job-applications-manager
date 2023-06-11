from django.db import models
import datetime
    
class Jobs(models.Model):
    
    description = models.CharField(max_length=2000)
    company_name = models.CharField(max_length=100)
    experience = models.IntegerField()
    job_id = models.CharField(max_length=100, null=True)
    job_url = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=200, null=True)
    skills_required = models.CharField(max_length=1000, null=True)
    publishing_time = models.DateTimeField(auto_now=True)
    last_date_of_application = models.DateField()
    test_date = models.DateField( null=True)
    interview_date = models.DateField( null=True)
