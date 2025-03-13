import sys, sweetify

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils.safestring import mark_safe

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
    user_servers = Server.objects.filter(created_by=request.user)
    user_projects = Project.objects.filter(created_by=request.user)
    return render(request, "professorHome.html", {"servers": user_servers, "projects": user_projects})

@login_required
def addProject(request):
    return render(request, "addProject.html", {})


@login_required
def addServer(request):
    if request.method == "POST":
        # Extract data from the form
        name = request.POST.get("server")
        operating_system = request.POST.get("operating_system")
        ip_address = request.POST.get("ip_address")
        software_installed = request.POST.get("software_installed", "")
        idrac_info = request.POST.get("idrac", "")
        notes = request.POST.get("special_notes", "")
        description = request.POST.get("project_purpose", "")

        # Create and save the server instance
        server = Server.objects.create(
            name=name,
            operating_system=operating_system,
            ip_address=ip_address,
            software_installed=software_installed,
            idrac_info=idrac_info,
            notes=notes,
            description=description,
            created_by=request.user
        )

        # Handle custom fields
        field_names = request.POST.getlist("custom_field_names[]")
        field_values = request.POST.getlist("custom_field_values[]")

        for name, value in zip(field_names, field_values):
            if name:  # Ensure the field has a name
                custom_field = CustomField.objects.create(name=name, value=value)
                server.custom_fields.add(custom_field)

        messages.success(request, "Server added successfully!")
        return redirect("home")  # Redirect to home page or a different page

    return render(request, "addServer.html")