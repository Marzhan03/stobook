from django import forms
from . import models


class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.CustomUser
        fields = ('username', 'email', 'date_of_birth', 'first_name', 'last_name', 'phone_number',)


class LoginForm(forms.ModelForm):
    class Meta:
        model = models.CustomUser
        fields = ('username', 'password',)