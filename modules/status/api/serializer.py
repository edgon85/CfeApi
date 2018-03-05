from rest_framework import serializers
from modules.status.models import Status

'''
JSON -- JavaScript Object Notation
'''

class StatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]

