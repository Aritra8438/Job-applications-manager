from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import JobApplicationSerializer
from .models import job_applications

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
