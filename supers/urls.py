from django.urls import path
from . import views

urlpatterns = [
    path('127.0.0.1:8000/api/supers/', views.super_list),
    path('127.0.0.1:8000/api/supers/<int:pk>/',views.supers_detail ),

]