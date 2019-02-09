from django.shortcuts import render
from chat.models import Message
from rest_framework import viewsets
# Create your views here.
from .serializers import MessageSerializer


#views.py with a DRF viewset configured to list and create messages


class ApiViewSet(viewsets.ModelViewSet):

    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    # def list(self, request):
    #     queryset = User.objects.all()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None):
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)

    # serializer_class = UserSerializer
    #     # queryset = User.objects.all()