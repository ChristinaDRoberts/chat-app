
from django.urls import path, include
from chat import views

urlpatterns = [
  # path('api/message/', views.ChatIndex.as_view(), name='apidata')
  # path('api/', include("api.urls")),
  path('api/message/', views.ChatIndex.as_view())

]

