from .views import *
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register("", views.JobsViewSet) 

urlpatterns = [
    path("hello/", hello),
]

urlpatterns+=router.urls