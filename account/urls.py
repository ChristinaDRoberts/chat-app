
# from django.urls import path
# from django.contrib.auth import auth_views
# from django.contrib.auth import (
#     REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
#     logout as auth_logout, update_session_auth_hash,
# )
#




from django.conf.urls import url
# from mysite.core import views as core_views
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.urls import path, include

app_name = "users"
urlpatterns = [
  path('login/', LoginView.as_view(template_name='registration/login.html'), name="login"),
  path('logout', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
  path('signup/', views.SignUp.as_view(), name='signup'),
  # url(r'^signup/$', core_views.signup, name='signup'),
]


# from django.views.generic.edit import CreateView
# from django.contrib.auth.forms import UserCreationForm
#
# urlpatterns =[
#
#     path('register/', CreateView.as_view(template_name='registration/register.html', form_class=UserCreationForm, success_url='/')),
#     url('accounts/', include('django.contrib.auth.urls')),
#
#     # rest of your URLs as normal
# ]
#


