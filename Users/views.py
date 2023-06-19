from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from Job_applications.serializers import JobApplicationSerializer

from .authentication import (
    create_access_token,
    create_refresh_token,
    decode_access_token,
    decode_refresh_token,
)
from .serializers import UserSerializer, ChangePasswordSerializer
from .models import User

from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated   

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
            raise AuthenticationFailed("Invalid credentials!")

        if not user.check_password(request.data["password"]):
            raise AuthenticationFailed("Invalid credentials!")

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        response = Response()

        response.set_cookie(key="refreshToken", value=refresh_token, httponly=False)
        response.data = {"token": access_token, "id": user.id, "refresh": refresh_token}

        return response


class UserAPIView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode("utf-8")
            id = decode_access_token(token)

            user = User.objects.filter(pk=id).first()
            response = Response()
            response.data = {
                "user": UserSerializer(user).data,
                "job_applications": JobApplicationSerializer(
                    user.job_application_set.all(), many=True
                ).data,
            }
            return response

        raise AuthenticationFailed("unauthenticated")


class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.POST["refresh"]
        if refresh_token is None:
            refresh_token = request.COOKIES.get("refreshToken")
        id = decode_refresh_token(refresh_token)
        print(id)
        _id = request.POST["id"]
        if str(id) != str(_id):
            raise AuthenticationFailed("unauthenticated")

        access_token = create_access_token(id)
        return Response({"token": access_token})


class LogoutAPIView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie(key="refreshToken")
        response.data = {"message": "success"}
        return response

class UpdatePassword(APIView):
    """
    An endpoint for changing password.
    """
    

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode("utf-8")
            id = decode_access_token(token)
            user = User.objects.get(id=id)
        
            serializer = ChangePasswordSerializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                old_password = serializer.data.get("old_password")
                if not user.check_password(old_password):
                    return Response({"old_password": ["Wrong password."]}, 
                                    status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                user.set_password(serializer.data.get("new_password"))
                user.save()
                response = Response(status=status.HTTP_204_NO_CONTENT)
                response.data = {"message": "success"}
                return response
               
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        raise AuthenticationFailed("unauthenticated")