from rest_framework import serializers
from modules.status.models import Status
from modules.accounts.api.serializer import UserPublicSerializer

from rest_framework.reverse import reverse as api_reverse

'''
JSON -- JavaScript Object Notation
'''

class StatusInLineUserSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Status
        fields = [
            'uri',
            'id',
            'content',
            'image'
        ]
    
    def get_uri(self, obj):
        # return '/api/status/{id}/'.format(id=obj.id)
        request = self.context.get('request')
        return api_reverse("api-status:detail", kwargs={"id": obj.id}, request=request)



class StatusSerializer(serializers.ModelSerializer):
    user    = UserPublicSerializer(read_only=True)  #Muestra la informacion del usuarion y ya no solo el id
    uri     = serializers.SerializerMethodField(read_only=True)  
    class Meta:
        model = Status
        fields = [
            'uri',
            'id',
            'user',
            'content',
            'image'
        ]
        read_only_fields = ['user']

    def get_uri(self, obj):
        # return '/api/status/{id}/'.format(id=obj.id)
        request = self.context.get('request')
        return api_reverse("api-status:detail", kwargs={"id": obj.id}, request=request)



    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required.")
        return data


