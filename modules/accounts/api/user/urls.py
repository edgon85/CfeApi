from django.urls import path, re_path
from .views import UserDetailAPIView

app_name = 'api_user'

urlpatterns = [
    re_path(r'^(?P<username>\w+)/$', UserDetailAPIView.as_view(), name='detail'),
    
]