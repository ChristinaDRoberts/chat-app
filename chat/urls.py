from django.urls import path
from . import views


#urls.py with a route configured for / that will load the ChatIndex

urlpatterns[
    path("/", views.ChatIndex.as_view)

]
