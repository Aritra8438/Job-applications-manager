from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import JobApplicationSerializer
from .models import job_applications

from pyresparser import ResumeParser


# Create your views here.
class ApplicationView(APIView):
    def post(self, request):
        serializer = JobApplicationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        application = job_applications.objects.all()
        serializer = JobApplicationSerializer(application, many=True)
        return Response(serializer.data)


def hello(request):
    print("Hello, Came here")
    data = ResumeParser("abc.pdf").get_extracted_data()
    return JsonResponse(data)
