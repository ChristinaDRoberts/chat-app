from django.urls import path
from . import views
from .models import Message
from api.views import ApiViewSet


#urls.py with a route configured for / that will load the ChatIndex

urlpatterns = [

    path('', views.ChatIndex.as_view(),name='chat')
         ]

