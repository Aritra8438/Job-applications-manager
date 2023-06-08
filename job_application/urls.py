from django.contrib import admin
from django.urls import path
from .views import ApplicationView, hello

urlpatterns = [path("", ApplicationView.as_view()), path("hello", hello)]
