from rest_framework.serializers import ModelSerializer
from .models import User, CV
from rest_framework import serializers
class CVSerializer(ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = CV
        fields = ['job_type', 'resume', 'resume_name', 'user']


class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user    


    