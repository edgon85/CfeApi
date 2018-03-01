import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

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

