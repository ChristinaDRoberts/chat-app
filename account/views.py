from django.shortcuts import render





# views.py with a view for signing up that uses the signup form.


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm
from django.views.generic import TemplateView
# from django.views import RegistrationView


class SignUp(generic.CreateView):
   form_class = SignUpForm
   success_url = reverse_lazy('account:login')
   template_name = 'registration/signup.html'

class MarketingView(TemplateView):
   template_name = "registration/index.html"














