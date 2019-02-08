from django.shortcuts import render





# views.py with a view for signing up that uses the signup form.


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm
# from django.views import RegistrationView


class SignUp(generic.CreateView):
   form_class = SignUpForm
   success_url = reverse_lazy('login')
   template_name = 'registration/signup.html'











# from django.contrib.auth import login, authenticate
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
#
#
#
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/signup.html', {'form': form})












