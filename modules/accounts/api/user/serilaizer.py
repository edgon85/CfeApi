import datetime
from django.contrib.auth import get_user_model
from django.utils import timezone

from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from modules.status.api.serializer import StatusInLineUserSerializer

User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    uri         = serializers.SerializerMethodField(read_only=True)
    status_list = serializers.SerializerMethodField(read_only=True)
    

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri',
            'status_list'
        ]
    
    def get_uri(self, obj):
        # return '/api/user/{id}/'.format(id=obj.id)
        request = self.context.get('request')
        return api_reverse("api_user:detail", kwargs={"username": obj.username}, request=request)

    def get_status_list(self, obj):
        request = self.context.get('request')
        qs = obj.status_set.all()
        return StatusInLineUserSerializer(qs, many=True, context={'request':request}).data