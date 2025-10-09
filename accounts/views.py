from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, ProfileUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from django.shortcuts import redirect

User = get_user_model()

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'authentication/register.html'

class LogInView(LoginView):
    template_name = 'authentication/login.html'
    success_url = reverse_lazy('home')


class ProfileView(LoginRequiredMixin, UpdateView ):
    model = User
    template_name = 'profile.html'
    form_class = ProfileUpdateForm
    context_object_name = 'user'

    def get_success_url(self):
        return  reverse_lazy('profile',kwargs={'pk': self.request.user.pk})

    