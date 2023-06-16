from .views import *
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("", views.JobsViewSet)

urlpatterns = [
    path("hello/", hello),
    path("register/", views.RegisterAPIView.as_view()),
    path("login/", views.LoginAPIView.as_view()),
    path("refresh/", views.RefreshAPIView.as_view()),
    path("logout/", views.LogoutAPIView.as_view()),
    path("update/", views.UpdateJobsAPIView.as_view()),
]

urlpatterns += router.urls
