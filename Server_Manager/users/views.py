from Server_Manager.auth_backend import PasswordlessAuthBackend
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            messages.success(request, 'User Registered')
            form.save()
            return redirect('/')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)

    else:
        form = RegistrationForm(request.POST)

    return render(request, 'users/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:

            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('profHome')
        else:
            messages.error(request, 'Login Failed - Try Again')


    else:
        form = LoginForm(request.POST)

    return render(request, 'website/login.html', {'form': form})