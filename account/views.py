from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, logout
from account.forms import RegisterForm, LoginForm

from account.models import CustomUser


def login(request):
    form=forms.LoginForm()
    if request.method == 'POST':
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)

                return redirect('/')

    return render(request, 'account/login.html')

    

def my_logout(request):
    logout(request)
    return redirect('home')


def register(request):
    form = RegisterForm(request.POST)
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            register=form.save(commi=False)
            register.save()
            return render(request, "account/login.html")  # Перенаправление на страницу успешной регистрации

        else:
            form = RegisterForm()
            return render(request, "account/register.html", context={
                'form': form, 'name': 'Marzhan'
            })

    return render(request, "account/register.html")
