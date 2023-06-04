from django.contrib import admin
from django.urls import path
from .views import UserView

urlpatterns = [
    path('register/', UserView.as_view()),    
]