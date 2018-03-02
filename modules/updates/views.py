import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from django.core.serializers import serialize

from cfeapi.mixins import JsonResponseMixin

from .models import Update

# Create your views here.

def json_example_view(request):
    '''
    URI -- for a REST API
    GET -- Retrive
    '''
    data = {
        "count": 1000,
        "content": "Some new content"
    }
    json_data = json.dumps(data)
    # return JsonResponse(data)
    return HttpResponse(json_data, content_type='application/json')

class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new data"
        }
        return JsonResponse(data)

class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new data"
        }
        return self.render_to_json_response(data)


class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        queryset = Update.objects.all()
        json_data = Update.objects.all().serialize()
        return HttpResponse(json_data, content_type='application/json')


