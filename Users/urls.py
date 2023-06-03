from django.contrib import admin
from django.urls import path
from .views import RegisterView, ShowRegisteredUser

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('showuser/<params>/', ShowRegisteredUser.as_view())
]