
from django.urls import path
from chat import views

#come back - urls.py with a route configured for api/message/

urlpatterns = [
  path('api/message', views.ChatIndex.as_view())

]
