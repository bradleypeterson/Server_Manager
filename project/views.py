from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib import messages

from project.forms import ProjectForm
from project.forms import ServerForm
from project.models import Project, Server
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

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    messages.success(request, "Project deleted successfully!")
    return redirect('home')

@login_required
def delete_server(request, server_id):
    server = get_object_or_404(Server, id=server_id)
    server.delete()
    messages.success(request, "Server deleted successfully!")
    return redirect('home')

@login_required
def delete_group(request, group_id):
    group = get_object_or_404(Group, group_id=group_id)
    group.delete()
    messages.success(request, "Group deleted successfully!")
    return redirect('home')