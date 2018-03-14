from django.urls import path, re_path
from .views import UserDetailAPIView

urlpatterns = [
    re_path(r'^(?P<username>\w+)/$', UserDetailAPIView.as_view(), name='detail'),
    
]