from django.contrib import admin
from django.urls import include, path

from pizza import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order/', views.order, name='order'),
]
