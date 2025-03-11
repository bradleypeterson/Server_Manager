from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .forms import LoginForm, RegistrationForm, ResetPasswordForm
from django.contrib import messages
from django.urls import reverse

from .models import AppUser


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

# class LoginView(View):
#     def get(self, request):
#         form = LoginForm(request.POST)
#         return render(request, 'login.html', {'form': form})
#     def post(self, request):
#         form = LoginForm(request.POST)
#
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             messages.success(request, 'Login Successful')
#             login(request, user)
#             if user.role == 'student':
#                 return redirect('studentHome', user.id)
#             else:
#                 request.session['userId'] = user.id
#                 return redirect('profHome', user.id)
#
#         else:
#             messages.error(request, 'Login Failed - Try Again')
#         return render(request, 'login.html', {'form': form})

def PasswordResetView(View):
    def get(self, request, user_id):
        form = ResetPasswordForm(request.POST)
        return render(request, "resetPassword.html", {'form': form, 'user_id': user_id})
    def post(self, request, user_id):
        form = ResetPasswordForm(request.POST)
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
        else:
            user = get_object_or_404(AppUser, id=user_id)
            user.set_password(password1)
            user.save()
            messages.success(request, 'Password Reset Successful')
            return redirect('/')
        return render(request, "resetPassword.html", {'form': form, 'user_id': user_id})

@login_required
def home(request):
    return render(request, "professorHome.html", {})

@login_required
def addProject(request):
    return render(request, "addProject.html", {})

@login_required
def addServer(request):
    return render(request, "addServer.html", {})