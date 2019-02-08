
# from django.urls import path
# from django.contrib.auth import auth_views
# from django.contrib.auth import (
#     REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
#     logout as auth_logout, update_session_auth_hash,
# )
#






from django.contrib.auth.views import LoginView

from django.urls import path
from . import views
app_name = "users"
urlpatterns = [
  path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
]


