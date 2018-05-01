"""cfeapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls

from modules.updates.views import (
    json_example_view, 
    JsonCBV, JsonCBV2, 
    SerializedListView, 
    SerializedDetailView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('api/', TemplateView.as_view(template_name='api-home.html'), name='home'),
    path('api/', include_docs_urls(title='Dj Ionic APIs')),
    path('api/status/', include('modules.status.api.urls', namespace='api-status')),
    path('api/updates/', include('modules.updates.api.urls')), # api/updates/ --> list api/updates/1/  --> detail 
    path('api/auth/', include('modules.accounts.api.urls')),
    path('api/user/', include('modules.accounts.api.user.urls', namespace='api_user')),
 
]
