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

            selected_user_ids = request.POST.getlist('users')
            selected_users = AppUser.objects.filter(id__in=selected_user_ids)
            group.users.set(selected_users)

            selected_project_ids = request.POST.getlist('projects')
            selected_projects = Project.objects.filter(id__in=selected_project_ids)
            unselected_projects = Project.objects.exclude(id__in=selected_project_ids)
            for project in selected_projects:
                project.groups.add(group)
                project.save()
            for project in unselected_projects:
                project.groups.remove(group)
                project.save()

            form.save_m2m()

            messages.success(request, "Group added successfully!")
            return redirect('home')
        return render(request, 'group/group.html', {'form': form})

def groupList(request):
    groups = Group.objects.all()

    return render(request, 'group/groupList.html', {'groups': groups})