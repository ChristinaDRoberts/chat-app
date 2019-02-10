from django.urls import path
from . import views


#urls.py with a route configured for / that will load the ChatIndex

urlpatterns = [

    path('', views.ChatIndex.as_view({
            'get': queryset,  # GET method should list objects
            'post': data,  # POST method should create object
    }))
    ]
# {
#             'get': queryset,  # GET method should list objects
#             'post': data,  # POST method should create object
#         }