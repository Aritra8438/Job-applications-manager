from django.urls import path
from .views import ApplicationView, ApplicationByIdView

urlpatterns = [
    path("", ApplicationView.as_view()),
    path("<int:pk>", ApplicationByIdView.as_view()),
]
