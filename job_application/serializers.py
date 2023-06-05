from rest_framework import serializers
from .models import job_applications

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = job_applications
        fields = "__all__"