import sys, sweetify

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils.safestring import mark_safe
import json, subprocess, os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from project.forms import ServerForm, ProjectForm
from .forms import LoginForm, RegistrationForm, ResetPasswordForm
from django.contrib import messages
from django.urls import reverse
from .models import AppUser
from project.models import Server, Project
from django.db.models import Q


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
    # Get projects where the user is directly linked, in a group linked to the project, or is the creator.
    user_projects = Project.objects.filter(
        Q(users=request.user) |
        Q(groups__users=request.user) |
        Q(created_by=request.user)
    ).distinct()

    # Get servers that are linked to any of these projects or directly created by the user.
    user_servers = Server.objects.filter(
        Q(project__in=user_projects) |
        Q(created_by=request.user)
    ).distinct()

    return render(request, "professorHome.html", {"projects": user_projects, "servers": user_servers})

@login_required
def viewProject(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.updated_by = request.user
            project.save()
            messages.success(request, "Project updated successfully!")
            return redirect('home')
        else:
            messages.error(request, "Update failed. Please correct the errors below.")
    else:
        form = ProjectForm(instance=project)

    return render(request, "addProject.html", {"form": form, "edit": True})

@login_required
def viewServer(request, server_id):
    server = get_object_or_404(Server, id=server_id)

    if request.method == "POST":
        form = ServerForm(request.POST, instance=server)
        if form.is_valid():
            server = form.save(commit=False)
            server.updated_by = request.user
            server.save()
            messages.success(request, "Server updated successfully!")
            return redirect('home')
        else:
            messages.error(request, "Update failed. Please correct the errors below.")
    else:
        form = ServerForm(instance=server)

    return render(request, "addServer.html", {"form": form, "edit": True})

@csrf_exempt
def ping_server(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            ip_address = data.get("ip_address")

            if not ip_address:
                return JsonResponse({"error": "No IP address provided"}, status=400)

            if os.name == "nt":
                command = ["ping", "-n", "1", ip_address]
            else:
                command = ["ping", "-c", "1", ip_address]

            result = subprocess.run(command, capture_output=True, text=True)

            print(f"Return code: {result.returncode}")
            print(f"Output:\n{result.stdout}")
            print(f"Error:\n{result.stderr}")

            if result.returncode == 0:
                output = result.stdout.splitlines()

                time_line = [line for line in output if "time=" in line or "time<" in line]
                if time_line:
                    time = time_line[0].split("time=")[-1].split(" ")[0] if "time=" in time_line[0] else \
                    time_line[0].split("time<")[-1].split(" ")[0]
                    return JsonResponse({
                        "status": "active",
                        "time": time,
                        "message": "Ping successful"
                    })
                else:
                    return JsonResponse({
                        "status": "inactive",
                        "message": "Ping failed - no time data"
                    })
            else:
                return JsonResponse({
                    "status": "inactive",
                    "message": "Ping failed",
                    "error": result.stderr
                })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)