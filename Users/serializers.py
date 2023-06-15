from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "password", "username"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            name=validated_data["name"],
            username=validated_data["username"],
            is_staff=False,
            is_superuser=False,
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
