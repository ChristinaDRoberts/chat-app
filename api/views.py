from django.shortcuts import render
from chat.models import Message
from rest_framework import viewsets
from .serializers import MessageSerializer
from django.utils.timezone import now
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import mixins



#views.py with a DRF viewset configured to list and create messages

# class CsrfExemptSessionAuthentication(SessionAuthentication):
#
#     def enforce_csrf(self, request):
#         return  # To not perform the csrf check previously happening


class ApiViewSet(viewsets.ModelViewSet, mixins.RetrieveModelMixin):

    serializer_class = MessageSerializer
    queryset = Message.objects.all().order_by('-id')[:10]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user, created=now())



