from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException, AuthenticationFailed
from Job_applications.serializers import JobApplicationSerializer
from rest_framework.permissions import IsAuthenticated

from .authentication import (
    create_access_token,
    create_refresh_token,
    decode_access_token,
    decode_refresh_token,
)
from .serializers import UserSerializer
from .models import User


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginAPIView(APIView):
    def post(self, request):
        user = User.objects.filter(email=request.data["email"]).first()

        if not user:
            raise APIException("Invalid credentials!")

        if not user.check_password(request.data["password"]):
            raise APIException("Invalid credentials!")
        
        user.is_active = True
        
        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        response = Response()

        response.set_cookie(key="refreshToken", value=refresh_token, httponly=True)
        response.data = {"token": access_token}

        return response


class UserAPIView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()
        
        if auth and len(auth) == 2:
            token = auth[1].decode("utf-8")
            id = decode_access_token(token)
            
            user = User.objects.filter(pk=id).first()
            print(user.job_application_set.all())
            response = Response()
            response.data = {"user": UserSerializer(user).data, 
                            "job_applications": JobApplicationSerializer(user.job_application_set.all(), many = True).data, 
                             }
            return response

        raise AuthenticationFailed("unauthenticated")


class RefreshAPIView(APIView):
    
    def post(self, request):
        refresh_token = request.COOKIES.get("refreshToken")
        id = decode_refresh_token(refresh_token)
        access_token = create_access_token(id)
        
        user = User.objects.get(id=id)
        
                 
        if(user.is_active) :
            access_token = create_access_token(id)
            return Response({"token": access_token})
        raise AuthenticationFailed("unauthenticated")
        
        


class LogoutAPIView(APIView):
    def post(self, request):
        response = Response()
        refresh_token = request.COOKIES.get("refreshToken")
        id = decode_refresh_token(refresh_token)
        user = User.objects.get(id=id)
        print(user.is_active)
        user.is_active = False
        user.save()
        response.delete_cookie(key="refreshToken")
        response.data = {"message": "success"}
        return response
