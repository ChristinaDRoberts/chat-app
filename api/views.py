from django.shortcuts import render
from chat.models import Message
from rest_framework import viewsets
# Create your views here.
from .serializers import MessageSerializer


#views.py with a DRF viewset configured to list and create messages


class ApiViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()