from django.urls import path, include
from . import views

urlpatterns = [
    path("register/", views.RegisterAPIView.as_view()),
    path("login/", views.LoginAPIView.as_view()),
    path("", views.UserAPIView.as_view()),
    path("refresh/", views.RefreshAPIView.as_view()),
    path("logout/", views.LogoutAPIView.as_view()),
    path("change-password/", views.UpdatePassword.as_view()),
    path(
        "password-reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
]
