from django.contrib.auth import get_user_model
from .forms import RegisterForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
User = get_user_model()
from django.views.generic import CreateView
# Create your views here.

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success = '/accounts/login/'