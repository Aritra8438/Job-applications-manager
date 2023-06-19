from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from .serializers import JobApplicationSerializer
from .models import Job_application
from Users.models import User
from Users.authentication import decode_access_token


# Create your views here.
class ApplicationView(APIView):
    def post(self, request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode("utf-8")
            id = decode_access_token(token)

            user = User.objects.filter(pk=id).first()
            serializer = JobApplicationSerializer(
                data=request.data, context={"user": user}
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

        raise AuthenticationFailed("unauthenticated")

    def get(self, request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode("utf-8")
            id = decode_access_token(token)

            user = User.objects.filter(pk=id).first()
            job_applications = Job_application.objects.filter(user=user)
            serializer = JobApplicationSerializer(job_applications, many=True)
            return Response(serializer.data)

        raise AuthenticationFailed("unauthenticated")


class ApplicationByIdView(APIView):
    def get(self, request, pk):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode("utf-8")
            id = decode_access_token(token)

            user = User.objects.filter(pk=id).first()
            job_application = Job_application.objects.get(id=pk)
            if job_application.user != user:
                raise AuthenticationFailed("unauthenticated")
            serializer = JobApplicationSerializer(job_application)
            return Response(serializer.data)

        raise AuthenticationFailed("unauthenticated")

    def patch(self, request, pk):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode("utf-8")
            id = decode_access_token(token)

            user = User.objects.filter(id=id).first()
            job_application = Job_application.objects.get(id=pk)
            if job_application.user != user:
                raise AuthenticationFailed("unauthenticated")
            serializer = JobApplicationSerializer(
                job_application, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

        raise AuthenticationFailed("unauthenticated")

    def delete(self, request, pk):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode("utf-8")
            id = decode_access_token(token)

            user = User.objects.filter(id=id).first()
            job_application = Job_application.objects.get(id=pk)
            if job_application.user != user:
                raise AuthenticationFailed("unauthenticated")
            job_application.delete()
            return Response("Job-application deleted", status=200)

        raise AuthenticationFailed("unauthenticated")
