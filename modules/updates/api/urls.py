from django.urls import path, re_path
from .views import (
    UpdateModelDetailAPIView, 
    UpdateModelListAPIView)

urlpatterns = [
    path('', UpdateModelListAPIView.as_view()),
    re_path(r'^(?P<id>\d+)', UpdateModelDetailAPIView.as_view()),
]