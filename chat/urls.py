from django.urls import path
from . import views


#urls.py with a route configured for / that will load the ChatIndex

urlpatterns = [

    path('', views.ChatIndex.as_view({
            'get': 'list',  # GET method should list objects
            'post': 'create',  # POST method should create object
        }), name='chat'),
    ]