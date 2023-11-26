from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, logout
from account.forms import RegisterForm, LoginForm

from account.models import CustomUser


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)

        return redirect('/')

    return render(request, 'account/login.html')

    

def my_logout(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        date_of_birth = request.POST.get("date_of_birth")

        form = RegisterForm(request.POST)

        if form.is_valid():
            CustomUser.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                email=email,
                last_name=last_name,
                phone_number=phone_number,
                date_of_birth=date_of_birth,
            )

            return render(request, "account/login.html")
        else:
            return render(request, "account/register.html", context={
                'form': form, 'name': 'Marzhan'
            })

    return render(request, "account/register.html")
