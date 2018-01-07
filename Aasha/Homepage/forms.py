from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class registerForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    class Meta:

        model = User
        help_texts = {
            'username': None,
            'password1': 'Enter your valid password'

        }
        fields = ('username', 'birth_date', 'password1', 'password2')





