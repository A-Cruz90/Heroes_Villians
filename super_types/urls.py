from django.urls import path
from . import views

urlpatterns = [
    path('127.0.0.1:8000/api/super_types/') ,
    path('127.0.0.1:8000/api/super_types/<int:pk>/')
]