from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm, ResetPasswordForm
from django.contrib import messages

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

def password_reset(request):
    form = ResetPasswordForm(request.POST)
    return render(request, "resetPassword.html", {'form': form})

@login_required
def home(request):
    return render(request, "professorHome.html", {})