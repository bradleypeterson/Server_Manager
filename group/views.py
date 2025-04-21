from django.shortcuts import render, redirect
from django.views import View

from project.models import Project
from .forms import GroupForm
from .models import Group
from user.models import  AppUser
from django.contrib.auth.decorators import login_required
from django.contrib import messages

class CreateGroupView(View):
    def get(self, request):
        form = GroupForm()
        return render(request, 'group/group.html', {'form': form})
    def post(self, request):
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()

            selected_users = request.POST.getlist('users')
            selected_projects = request.POST.getlist('projects')

            selected_users = AppUser.objects.filter(id__in=selected_users)
            selected_projects = Project.objects.filter(id__in=selected_projects)

            for project in selected_projects:
                project.groups.add(group)
            for user in selected_users:
                group.users.add(user)

            group.save()

            messages.success(request, "Group added successfully!")
            return redirect('home')
        return render(request, 'group/group.html', {'form': form})