
from django.urls import path, include
from chat import views
from api.views import ApiViewSet

urlpatterns = [
  # path('api/message/', views.ChatIndex.as_view(), name='apidata')
  # path('api/', include("api.urls")),
  path('message/', ApiViewSet.as_view({'serialize_class': 'queryset'}))

]

