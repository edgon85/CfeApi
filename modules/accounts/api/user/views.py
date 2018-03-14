from django.contrib.auth import get_user_model

from rest_framework import permissions, generics

from .serilaizer import UserDetailSerializer
from modules.accounts.api.permissions import AnonPermissionOnly


User = get_user_model()


class UserDetailAPIView(generics.RetrieveAPIView):
    # permission_classes      = [permissions.IsAuthenticatedOrReadOnly]
    queryset                = User.objects.filter(is_active=True)
    serializer_class        = UserDetailSerializer
    lookup_field            = 'username'