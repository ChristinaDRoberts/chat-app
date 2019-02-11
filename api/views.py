from django.shortcuts import render
from chat.models import Message
from rest_framework import viewsets
from .serializers import MessageSerializer
from django.utils.timezone import now




#views.py with a DRF viewset configured to list and create messages


class ApiViewSet(viewsets.ModelViewSet):

    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, created=now())



