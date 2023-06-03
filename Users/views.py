from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User


# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class ShowRegisteredUser(APIView):
    def get(self, request, params):
        print(params)
        user = User.objects.filter(email=params).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
