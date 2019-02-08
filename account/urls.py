

from django.contrib.auth import auth_views


urlpatterns = [

    path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('logout/', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),


]
