from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages

from project.forms import ProjectForm
from project.forms import ServerForm
from user.models import AppUser
from group.models import Group

# Create your views here.
class AddProjectView(View):
    def get(self, request):
        form = ProjectForm(request.POST or None)
        return render(request, "addProject.html", {'form': form})
    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)  # Do not save yet
            project.created_by = request.user  # Set created_by
            project.updated_by = request.user  # Set created_by
            project.save()  # Now save the instance

            selected_users = form.cleaned_data['available_users']
            selected_groups = form.cleaned_data['available_groups']

            selected_groups = Group.objects.filter(group_id__in=selected_groups)

            project.users.set(selected_users)
            project.groups.set(selected_groups)

            project.save()  # Now save the instance

            messages.success(request, "Project added successfully!")
            return redirect('home')
        else:
            messages.error(request, "Form submission failed. Please correct the errors below.")
            return render(request, "addProject.html", {'form': form})

class AddServerView(View):
    def get(self, request):
        form = ServerForm()
        return render(request, "addServer.html", {'form': form})

    def post(self, request):
        form = ServerForm(request.POST)
        if form.is_valid():
            server = form.save(commit=False)  # Do not save yet
            server.created_by = request.user  # Set created_by
            server.updated_by = request.user  # Set created_by
            server.save()  # Now save the instance
            messages.success(request, "Server added successfully!")
            return redirect('home')
        else:
            messages.error(request, "Form submission failed. Please correct the errors below.")
            return render(request, "addServer.html", {'form': form})