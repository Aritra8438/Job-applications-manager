from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import JobApplicationSerializer
from .models import Job_application
from Users.models import User
from Users.authentication import decode_refresh_token

# Create your views here.
class ApplicationView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get("refreshToken")
        id = decode_refresh_token(refresh_token)
        user = User.objects.get(id=id)
        serializer = JobApplicationSerializer(data=request.data, context= {'user':user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        application = Job_application.objects.all()
        print(application)
        applications = []
        for app in application:
            user = app.user
            refresh_token = request.COOKIES.get("refreshToken")
            id = decode_refresh_token(refresh_token)
            print(id)
            
            if user.id == id :
                applications.append(app)
        serializer = JobApplicationSerializer(applications, many=True)
        return Response(serializer.data)
