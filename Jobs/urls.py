from .views import *
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router=DefaultRouter()
router.register("", views.JobsViewSet) 
# router.register("reminderview", views.ReminderViewSet)
urlpatterns = [
    path("hello/", hello),
    path('reminder/', views.ReminderViewSet.as_view({'get': 'List'})),
    
]

urlpatterns+=router.urls