from django import forms
from . import models
from django.core.validators import MaxLengthValidator,RegexValidator

class RegisterForm(forms.ModelForm):
    username=forms.CharField(
        validators=[MaxLengthValidator(limit_value=30)]
    )
    email=forms.EmailField()
    date_of_birth = forms.DateField()

    first_name = forms.CharField(
         validators=[
            MaxLengthValidator(limit_value=30),
            RegexValidator(
                regex=r'^[a-zA-Z][a-zA-Z0-9_]{4-31}$',
                message="Введите правильно",
                code="invalid_first_number",
            )
            ]
    )

    last_name = forms.CharField(
         validators=[
            MaxLengthValidator(limit_value=30),
            RegexValidator(
                regex=r'^[a-zA-Z][a-zA-Z0-9_]{4-31}$',
                message="Введите правильную фамлию",
                code="invalid_last_name",
            )]
    )

    phone_number = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^\+77\d{9}$',
                message="Введите номер телефона в формате +7хххххххххх",
                code="invalid_phone_number",
            )
        ]
    )
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        
        return password2

    is_active = forms.BooleanField()

    is_admin = forms.BooleanField()
    class Meta:
        model = models.CustomUser
        fields = ('username', 'email', 'date_of_birth', 'first_name', 'last_name', 'phone_number','is_active','password')


class LoginForm(forms.ModelForm):
    username=forms.CharField(
        validators=[
            MaxLengthValidator(limit_value=30),
            RegexValidator(
                regex=r'^[a-zA-Z][a-zA-Z0-9_]{4-31}$',
                message="Введите правильную фамлию",
                code="invalid_last_name",
            )]
    )
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        
        return password2

    class Meta:
        model = models.CustomUser
        fields = ('username', 'password',)