from django.urls import path, re_path
from .views import (
    # StatusListSearchAPIView,
    StatusAPIView,
    # StatusCreateAPIView,
    StatusDetailAPIView,
    # StatusUpdateAPIView,
    # StatusDeleteAPIView,
)

app_name = 'api-status'
urlpatterns = [
    path('', StatusAPIView.as_view()),
    re_path(r'^(?P<id>\d+)/$', StatusDetailAPIView.as_view(), name='detail'),
    # re_path(r'^(?P<id>\d+)/update/$', StatusUpdateAPIView.as_view()),
    # re_path(r'^(?P<id>\d+)/delete/$', StatusDeleteAPIView.as_view()),
]