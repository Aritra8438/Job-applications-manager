from rest_framework.authentication import get_authorization_header
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.exceptions import APIException, AuthenticationFailed
from .models import Jobs, Company
from .serializers import JobsSerializer, CompanySerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from Users.authentication import *


def hello(request):
    return HttpResponse("Awesome, vercel app is running")


class JobsViewSet(ModelViewSet):
    serializer_class = JobsSerializer
    queryset = Jobs.objects.all()

    def create(self, request, *args, **kwargs):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode("utf-8")
            id = decode_access_token(token)

            company = Company.objects.filter(pk=id).first()
            serializer = JobsSerializer(data=request.data, context={"company": company})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

        raise AuthenticationFailed("unauthenticated")
        return super().create(request, *args, **kwargs)

    def list(self, request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode("utf-8")
            id = decode_access_token(token)

            company = Company.objects.filter(pk=id).first()

            queryset = Jobs.objects.filter(company_id=company.id)
            serializer = JobsSerializer(queryset, many=True)
            return Response(serializer.data)
        raise AuthenticationFailed("unauthenticated")

    def partial_update(self, request, pk=None):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode("utf-8")
            id = decode_access_token(token)

            company = Company.objects.filter(pk=id).first()
            queryset = Jobs.objects.filter(company_id=company.id)
            job = get_object_or_404(queryset, pk=pk)
            serializer = self.get_serializer(job, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        raise AuthenticationFailed("unauthenticated")

    def destroy(self, request, pk=None):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode("utf-8")
            id = decode_access_token(token)

            company = Company.objects.filter(pk=id).first()
            queryset = Jobs.objects.filter(company_id=company.id)

            job = get_object_or_404(queryset, pk=pk)
            self.perform_destroy(job)
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise AuthenticationFailed("unauthenticated")


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

        access_token = create_access_token(company.id)
        refresh_token = create_refresh_token(company.id)

        response = Response()

        response.set_cookie(key="refreshToken", value=refresh_token, httponly=True)
        response.data = {"token": access_token}

        return response


class CompanyAPIView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode("utf-8")
            id = decode_access_token(token)
            company = Company.objects.filter(pk=id).first()

            return Response(CompanySerializer(company).data)

        raise AuthenticationFailed("unauthenticated")


class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get("refreshToken")
        id = decode_refresh_token(refresh_token)
        access_token = create_access_token(id)
        return Response({"token": access_token})


class LogoutAPIView(APIView):
    def post(self, _):
        response = Response()
        response.delete_cookie(key="refreshToken")
        response.data = {"message": "success"}
        return response
