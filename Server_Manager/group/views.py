from django.shortcuts import render, redirect
from .forms import GroupForm
from .models import Group
from django.contrib.auth.decorators import login_required

@login_required
def createGroup(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()

            form.save_m2m()

            print("Group created successfully!")
            return redirect('group_list')

    else:
        form = GroupForm()

    return render(request, 'group/group.html', {'form': form})


def groupList(request):
    # Get all groups, you can customize this if needed
    groups = Group.objects.all()

    # Render the group list template with the groups
    return render(request, 'group/groupList.html', {'groups': groups})