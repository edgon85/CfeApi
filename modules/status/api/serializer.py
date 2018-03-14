from rest_framework import serializers
from modules.status.models import Status
from modules.accounts.api.serializer import UserPublicSerializer

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
        return '/api/status/{id}/'.format(id=obj.id)



class StatusSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)

    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image'
        ]
        read_only_fields = ['user']

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required.")
        return data


