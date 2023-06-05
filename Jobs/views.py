from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Jobs
from .serializers import JobsSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status


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
        
    
    
    
    
    
    
    
# Create your views here.
