from django.shortcuts import render
from chat.models import Message
# Create your views here.
from .serializers import MessageSerializer
django.contrib.auth.views.login


#views.py with a DRF viewset configured to list and create messages


