from django.urls import path, re_path
from .views import (
    StatusListSearchAPIView,
    StatusAPIView,
    StatusCreateAPIView,
    StatusDetailAPIView,
    # StatusUpdateAPIView,
    # StatusDeleteAPIView,
)

urlpatterns = [
    path('', StatusAPIView.as_view()),
    path('create/', StatusCreateAPIView.as_view()),
    re_path(r'^(?P<id>.*)/$', StatusDetailAPIView.as_view()),
    # re_path(r'^(?P<id>.*)/update/$', StatusUpdateAPIView.as_view()),
    # re_path(r'^(?P<id>.*)/delete/$', StatusDeleteAPIView.as_view()),
]