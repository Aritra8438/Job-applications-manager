from .views import *
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("job", views.JobsViewSet)

urlpatterns = [
    path("hello/", hello),
    path("register/", views.RegisterAPIView.as_view()),
    path("login/", views.LoginAPIView.as_view()),
    path("refresh/", views.RefreshAPIView.as_view()),
    path("logout/", views.LogoutAPIView.as_view()),
    path("view/", views.CompanyAPIView.as_view()),
    path("search/", views.SearchJobs),
]

urlpatterns += router.urls
