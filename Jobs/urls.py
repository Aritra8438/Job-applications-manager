from .views import *
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register("Jobs", views.JobsViewSet) 

urlpatterns = [
    path("", hello),
]

urlpatterns+=router.urls