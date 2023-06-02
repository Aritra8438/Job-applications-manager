from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Awesome, vercel app is running")
# Create your views here.
