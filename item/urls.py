from django.contrib import admin
from django.urls import path, include

from . import views
from core.views import index

app_name = "item"

urlpatterns = [
    path("new/", views.new, name="new"),
    path("<id>/", views.detail, name="detail"),
]
