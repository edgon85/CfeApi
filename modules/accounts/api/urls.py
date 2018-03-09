from django.urls import path
from .views import AuthView

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token #acounts app


urlpatterns = [
    path('', AuthView.as_view()),
    path('jwt/', obtain_jwt_token),  #acounts 
    path('jwt/refresh/', refresh_jwt_token),  
    
]
