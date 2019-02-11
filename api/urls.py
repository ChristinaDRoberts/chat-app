
from django.urls import path
from api.views import ApiViewSet

urlpatterns = [
 # since we are looking for json data from our api we need to have our message route
 # use the ApiViewSet
  path('message/', ApiViewSet.as_view({'get': 'list', 'post': 'create'}))

]
