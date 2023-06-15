from rest_framework import serializers
from .models import Job_application


class JobApplicationSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Job_application
        fields = ["job_url","status", "user"]
        read_only_fields = ['user']
    def create(self, validated_data):
        user = self.context['user']
        job_application = Job_application(
            job_url=validated_data["job_url"],
            status=validated_data["status"],
            user = user
        )
        print(user.id)
        job_application.save()
        return Job_application(**validated_data, user=user)
        return job_application