from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.views import View
from .authentication import (
    create_access_token,
    create_refresh_token,
    decode_access_token,
    decode_refresh_token,
)
from .serializers import UserSerializer, CVSerializer
from .models import User, CV
from django.http import HttpResponse
from rest_framework.authtoken.models import Token

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

        serializer = UserSerializer(user)

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        response = Response()

        response.set_cookie(key="refreshToken", value=refresh_token, httponly=True)
        response.data = {"token": access_token}

        return response

        return Response(serializer.data)


class UserAPIView(APIView):
    parser_classes= (JSONParser, FormParser, MultiPartParser)
    def get(self, request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode("utf-8")
            id = decode_access_token(token)

            user = User.objects.filter(pk=id).first()

            return Response(UserSerializer(user).data)

        raise AuthenticationFailed("unauthenticated")
    
    
    def post(self,request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)

            user = User.objects.filter(pk=id).first()
        request.user=user
        
        serializer=CVSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=200)
        
        return Response(serializer.errors, status=400)
        


class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get("refreshToken")
        id = decode_refresh_token(refresh_token)
        access_token = create_access_token(id)
        return Response({
            'token': access_token
        })

class ResumeAPIView(APIView):
    parser_classes= (JSONParser, FormParser, MultiPartParser)
    def get(self, request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)
            
            queryset = CV.get_all_CVs_by_user(id)
          
            result=[]
            
            for cv in queryset:
                result.append(CVSerializer(cv).data)
            response=Response()
            response.data = {
            'result': result
            }       

            return response

        raise AuthenticationFailed('unauthenticated')
    
class LogoutAPIView(APIView):
    def post(self, _):
        response = Response()
        response.delete_cookie(key="refreshToken")
        response.data = {"message": "success"}
        return response
    
    