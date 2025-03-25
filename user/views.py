import sys, sweetify

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils.safestring import mark_safe

from project.forms import ServerForm
from .forms import LoginForm, RegistrationForm, ResetPasswordForm
from django.contrib import messages
from django.urls import reverse

from .models import AppUser
from project.models import Server, CustomField, Project


# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = RegistrationForm(request.POST)
        return render(request, 'register.html', {'form': form})
    def post(self, request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            messages.success(request, 'User Registered')
            user = form.save()
            user.refresh_from_db()
            return redirect('/')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
        return render(request, 'register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'form': form})
    def post(self, request):
        form = LoginForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            messages.success(request, 'Login Successful')
            login(request, user)
            request.session['userId'] = user.id
            return redirect('/home/', user.id)
        else:
            messages.error(request, 'Login Failed - Try Again')
        return render(request, 'login.html', {'form': form})

@login_required
def password_reset(request, user_id):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
        else:
            user = get_object_or_404(AppUser, id=user_id)

            try:
                validate_password(password1, user)
            except ValidationError as e:
                err_msg = ''
                for error in e.messages:
                    err_msg += '<br>' + error + '<br>'
                sweetify.error(request, 'Invalid password', html=mark_safe(err_msg), persistent=True)
            else:
                user.set_password(password1)
                user.save()
                messages.success(request, 'Password Reset Successful')
                return redirect('/')


    else:
        form = ResetPasswordForm(request.POST)
    return render(request, "resetPassword.html", {'form': form, 'user_id': user_id})

@login_required
def home(request):
    user_projects = Project.objects.filter(users=request.user)
    user_servers = Server.objects.filter(created_by=request.user)
    return render(request, "professorHome.html", {"servers": user_servers, "projects": user_projects})

@login_required
def viewServer(request, server_id):
    server = get_object_or_404(Server, id=server_id)

    form = ServerForm(request.POST or None, instance=server)
    cleaned_data = form.cleaned_data if form.is_valid() else None
    print(form.is_valid())
    print(cleaned_data)
    print(form)
    return render(request, "addServer.html", {"form": form, "edit": True})