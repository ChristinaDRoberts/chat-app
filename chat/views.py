from django.shortcuts import render




from django.views.generic import TemplateView

#views.py with a ChatIndex view.






class ChatIndex(TemplateView):
    template_name = 'chat.html'


