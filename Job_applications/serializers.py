from rest_framework import serializers
from .models import Job_application


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_application
        fields = "__all__"
