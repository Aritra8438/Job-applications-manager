from .views import *
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from Users.views import RefreshAPIView, LogoutAPIView


router=DefaultRouter()
router.register("", views.JobsViewSet) 
# router.register("reminderview", views.ReminderViewSet)
urlpatterns = [
    path("hello/", hello),
    path('reminder/', views.ReminderViewSet.as_view({'get': 'List'})),
    path("register/", views.RegisterAPIView.as_view()),
    path("login/", views.LoginAPIView.as_view()),
    path("", views.UserAPIView.as_view()),
    path("jobs/", views.JobsAPIView.as_view()),
    path("refresh/", RefreshAPIView.as_view()),
    path("logout/", LogoutAPIView.as_view()),
    
]

urlpatterns+=router.urls