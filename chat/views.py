from django.shortcuts import render


from .models import Message
from rest_framework import viewsets
from api.serializer import


#views.py with a ChatIndex view.

class ChatIndex(viewsets.ModelViewSet):
    queryset = Message.objects.all()







