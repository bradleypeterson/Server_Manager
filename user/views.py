from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, RegistrationForm, ResetPasswordForm
from django.contrib import messages

from .models import AppUser


# Create your views here.
def register(request):
    if request.method == 'POST':
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

    else:
        form = RegistrationForm(request.POST)

    return render(request, 'register.html', {'form': form})



def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            messages.success(request, 'Login Successful')
            login(request, user)
            if user.role == 'student':
                return redirect('studentHome', user.id)
            else:
                request.session['userId'] = user.id
                return redirect('profHome', user.id)

        else:
            messages.error(request, 'Login Failed - Try Again')


    else:
        form = LoginForm(request.POST)

    return render(request, 'login.html', {'form': form})

def password_reset(request, user_id):
    if request.method == 'POST':
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
    else:
        form = ResetPasswordForm(request.POST)
    return render(request, "resetPassword.html", {'form': form, 'user_id': user_id})

@login_required
def home(request):
    return render(request, "professorHome.html", {})

@login_required
def addProject(request):
    return render(request, "addProject.html", {})