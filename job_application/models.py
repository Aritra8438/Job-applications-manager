from django.db import models
from Jobs.models import Jobs
from Users.models import User

status = (
    ('val1', 'Applied'),
    ('val2', 'Under Consideration'),
    ('val3', 'Interviewed'),
    ('val4', 'declined')
)
# Create your models here.
class job_applications(models.Model):
    id = models.IntegerField(primary_key=True)
    job_url = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    time = models.TimeField(auto_now_add=True)
    status = models.CharField(max_length=20,choices=status)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

