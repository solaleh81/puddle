from django.contrib import admin
from django.urls import path

from . import views
from .views import index, contact

urlpatterns = [
    path('', views.index, name="index"),
]