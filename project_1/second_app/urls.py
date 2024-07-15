
from django.urls import path, include
from  . import views

urlpatterns = [
    path('', views.home),
    path('courses/', views.courses),
    path('about/', views.about),
]
