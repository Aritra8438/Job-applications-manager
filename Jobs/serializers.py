from rest_framework import serializers
from .models import Jobs, Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        company = Company(
            email=validated_data["email"],
            name=validated_data["name"],
            username=validated_data["username"],
            head_quarters=validated_data["head_quarters"],
            openings=validated_data["openings"],
        )
        company.set_password(validated_data["password"])
        company.save()
        return company


class JobsSerializer(serializers.ModelSerializer):
    read_only_fields = ["company"]

    class Meta:
        model = Jobs
        fields = "__all__"

    def create(self, validated_data):
        company = self.context["company"]
        jobs = Jobs(
            **validated_data,
            company=company,
        )
        jobs.save()
        return jobs
