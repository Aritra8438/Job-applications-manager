from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    

    first_name = None
    last_name = None
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
class CV(models.Model):
    CHOICES = [
    ("Technical", "Technical"),
    ("Marketing", "Marketing"),
    ("Education", "Education"),
    ("Govt_Job", "Govt_job"),
    ]  


    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    job_type = models.CharField(max_length=100, choices=CHOICES)
    resume=models.FileField(upload_to='documents/')
    resume_name=models.CharField(max_length=50)
    
    @staticmethod
    def get_all_CVs_by_user(id):

        # Check if store ID was passed
        if id:
            return CV.objects.filter(user_id=id)
