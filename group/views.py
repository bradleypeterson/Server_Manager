from django.shortcuts import render, redirect
from django.views import View

from .forms import GroupForm
from .models import Group
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

            form.save_m2m()

            print("Group created successfully!")
            return redirect('group_list')
        return render(request, 'group/group.html', {'form': form})

def groupList(request):
    groups = Group.objects.all()

    return render(request, 'group/groupList.html', {'groups': groups})