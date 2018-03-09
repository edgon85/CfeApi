from django.views.generic import View
from django.http import HttpResponse

from modules.updates.models import Update as UpdateModel


# Creating, Updating, Deleting, Retriving (1) -- Update model

class UpdateModelDetailAPIView(View):
    '''
    Retrive, Update, Delete --> Objects
    '''

    def get(self, requet, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json') #json

    def post(self, request, *args, **kwargs):

        return HttpResponse({}, content_type="application/json")

    def put(self, request, *args, **kwargs):

        return HttpResponse({}, content_type="application/json")

    def delete(self, request, *args, **kwargs):

        return HttpResponse({}, content_type="application/json")

class UpdateModelListAPIView(View):
    '''
    List View
    Create View
    '''

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type="application/json")
        
    def post(self, request, *args, **kwargs):

        return HttpResponse({}, content_type="application/json")





