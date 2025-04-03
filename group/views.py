from django.shortcuts import render, redirect
from django.views import View

from .forms import GroupForm
from .models import Group
from user.models import  AppUser
from django.contrib.auth.decorators import login_required

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
            group.save()

            form.save_m2m()

            print("Group created successfully!")
            return redirect('group_list')
        return render(request, 'group/group.html', {'form': form})

def groupList(request):
    groups = Group.objects.all()

    return render(request, 'group/groupList.html', {'groups': groups})