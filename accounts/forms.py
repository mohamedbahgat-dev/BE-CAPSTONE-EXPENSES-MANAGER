from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'age','location', 'profile_picture')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','first_name', 'last_name', 'age' ,'profile_picture', 'location', 'language' ,'currency')
        widgets = {
            'profile_picture': forms.FileInput(),   # <-- plain file input
        }
