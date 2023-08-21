from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('privacy/', views.privacy, name='privacy'),
    path('delivery/', views.delivery, name='delivery'),
    path('about/', views.about, name='about'),
    path('club/', views.club, name='club'),
]
