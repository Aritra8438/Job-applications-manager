from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Jobs, Company
from .serializers import JobsSerializer, CompanySerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from datetime import datetime
from datetime import timedelta
from Users.models import User
from rest_framework.exceptions import APIException, AuthenticationFailed
from .utils import send_email
from Users.authentication import create_access_token, create_refresh_token, decode_access_token, decode_refresh_token
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.authentication import get_authorization_header

def hello(request):
    return HttpResponse("Awesome, vercel app is running")


class JobsViewSet(ModelViewSet):
    serializer_class = JobsSerializer
    queryset = Jobs.objects.all()
    
    def create(self, request, *args, **kwargs):        
        return super().create(request, *args, **kwargs)
    
    def list(self, request):
        queryset = Jobs.objects.all()
        serializer = JobsSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Jobs.objects.all()
        job = get_object_or_404(queryset, pk=pk)
        serializer = JobsSerializer(job)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        queryset = Jobs.objects.all()
        job = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(job, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def partial_update(self, request, pk=None):
        queryset = Jobs.objects.all()
        job = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(job, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        queryset = Jobs.objects.all()
        job = get_object_or_404(queryset, pk=pk)
        self.perform_destroy(job)
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class ReminderViewSet(ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer
    def List(self, request):
        queryset = Jobs.objects.all()  
        
        for job in queryset:
            serializer = JobsSerializer(job)
            
            last_date_to_apply = serializer.data['last_date_of_application']
            last_date_to_apply = datetime.strptime(last_date_to_apply, "%Y-%m-%d").date()
            
            if (last_date_to_apply - timezone.now().date()) < timedelta( days=5 )  :
                users = User.objects.all()
                for user in users:
                    email = user.email
                    send_email(request,email);
                
        response = Response()    
        response.data = {
            'message': 'success'
        }
        return response
          
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)    

class LoginAPIView(APIView):
    def post(self, request):
        company = Company.objects.filter(email=request.data["email"]).first()

        if not company:
            raise APIException("Invalid credentials!")

        if not company.check_password(request.data["password"]):
            raise APIException("Invalid credentials!")

        serializer = CompanySerializer(company)

        access_token = create_access_token(company.id)
        refresh_token = create_refresh_token(company.id)

        response = Response()

        response.set_cookie(key="refreshToken", value=refresh_token, httponly=True)
        response.data = {"token": access_token}

        return response
    
class UserAPIView(APIView):
    parser_classes= (JSONParser, FormParser, MultiPartParser)
    def get(self, request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode("utf-8")
            id = decode_access_token(token)

            user = Company.objects.filter(pk=id).first()

            return Response(CompanySerializer(user).data)

        raise AuthenticationFailed("unauthenticated")
    
    
    def post(self,request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)

            user = Company.objects.filter(pk=id).first()
        request.user=user
        
        serializer=JobsSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=200)
        
        return Response(serializer.errors, status=400)
    
class JobsAPIView(APIView):
    parser_classes= (JSONParser, FormParser, MultiPartParser)
    def get(self, request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)
            
            queryset = Jobs.get_all_Jobs_by_company(id)
          
            result=[]
            
            for job in queryset:
                result.append(JobsSerializer(job).data)
            response=Response()
            response.data = {
            'result': result
            }       

            return response

        raise AuthenticationFailed('unauthenticated')    
        
    
    
    
    
    
# Create your views here.
