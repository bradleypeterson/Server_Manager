from Server_Manager.auth_backend import PasswordlessAuthBackend
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import LoginForm
from django.contrib.auth import authenticate
import sweetify
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'User Registered')
            form.save()
            return redirect('/')
        else:
            messages.error(request, 'User Not Registered')

    else:
        form = UserCreationForm(request.POST)

    return render(request, 'users/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        return redirect('profHome')
        form = LoginForm(request.POST)
        user = authenticate(username=form.username)
        login(request, user)

    else:
        form = LoginForm()

    return render(request, 'website/login.html', {'form': form})