





# from mysite.core import views as core_views
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.urls import path
from .views import MarketingView

app_name = "account"

urlpatterns = [
  path('', MarketingView.as_view(), name="index"),
  path('login/', LoginView.as_view(template_name='registration/login.html'), name="login"),
  path('logout', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
  path('signup/', views.SignUp.as_view(), name='signup'),
]


