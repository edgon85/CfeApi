from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response

from modules.status.models import Status
from .serializer import StatusSerializer


class StatusListSearchAPIView(APIView):
    permission_classes      = []
    authentication_classes  = []

    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data) 

    def post(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)


# CreateModelMixin ---- POST method
# UpdateModelMixin ---- PUT method 
# DestroyModelMixin ---- DELETE Method

class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes      = []
    authentication_classes  = []

    # queryset                = Status.objects.all()
    serializer_class        = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes      = []
#     authentication_classes  = []

#     queryset                = Status.objects.all()
#     serializer_class        = StatusSerializer
#     lookup_field            = 'id'  # 'slug'


class StatusDetailAPIView(generics.RetrieveAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    permission_classes      = []
    authentication_classes  = []

    queryset                = Status.objects.all()
    serializer_class        = StatusSerializer
    lookup_field            = 'id'  # 'slug'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # class get_object(self, *args, **kwargs):
    #     '''
    #     Es lo mismo que lookup_field
    #     '''
    #     kwargs  = self.kwargs
    #     kw_id   = kwargs.get('id')
    #     return Status.objects.get(id=kw_id) 



# class StatusCreateAPIView(generics.CreateAPIView):
#     permission_classes      = []
#     authentication_classes  = []

#     queryset                = Status.objects.all()
#     serializer_class        = StatusSerializer

#     # def perform_create(serlf, serializer):
#     #     serializer.save(user=self.request.user)


# class StatusUpdateAPIView(generics.UpdateAPIView):
#     permission_classes      = []
#     authentication_classes  = []

#     queryset                = Status.objects.all()
#     serializer_class        = StatusSerializer
#     lookup_field            = 'id'  # 'slug'


# class StatusDeleteAPIView(generics.DestroyAPIView):
#     permission_classes      = []
#     authentication_classes  = []

#     queryset                = Status.objects.all()
#     serializer_class        = StatusSerializer
#     lookup_field            = 'id'  # 'slug'