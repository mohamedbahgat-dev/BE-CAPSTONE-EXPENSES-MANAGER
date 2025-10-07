from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'authentication/register.html'

class LogInView(LoginView):
    template_name = 'authentication/login.html'
    success_url = reverse_lazy('home')


