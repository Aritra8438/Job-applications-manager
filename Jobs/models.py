from django.db import models
from django.contrib.auth.models import AbstractUser
from Users.models import User

class Company(User):
   
    head_quarters = models.CharField(max_length=20)
    openings = models.IntegerField()
    
class Jobs(models.Model):
    
    description = models.CharField(max_length=2000)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    experience = models.IntegerField()
    job_id = models.CharField(max_length=100, null=True)
    job_url = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=200, null=True)
    skills_required = models.CharField(max_length=1000, null=True)
    publishing_time = models.DateTimeField(auto_now=True)
    # last_date_of_application = models.DateField()
    test_date = models.DateField( null=True)
    interview_date = models.DateField( null=True)
    
    @staticmethod
    def get_all_Jobs_by_company(id):

        # Check if store ID was passed
        if id:
            return Jobs.objects.filter(company_id=id)
