from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .models import Group
from .forms import GroupForm


# Create your views here.
def createGroup(request, id):
    course = Course.objects.get(pk=id)
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            try:
                instance = form.save(commit=False)
                instance.course = course;
                instance.save()
                return redirect('profHome')
            except:
                pass
    else:
        form = GroupForm()
        return render(request, 'group/createGroup.html', {'form': form, 'course': course})


def groupDetail(request, id):
    group = get_object_or_404(Group, pk=id)
    return render(request, "group/groupDetail.html", {"group": group})

def destroyGroup(request, id):
    group = Group.objects.get(id=id)
    group.delete()
    return redirect('profHome')

def editGroup(request, id):
    group = get_object_or_404(Group, pk=id)
    return render(request, "group/editGroup.html", {"group": group})

def updateGroup(request, id):
    group = Group.objects.get(id=id)
    form = GroupForm(request.POST, instance=group)
    if form.is_valid():
        form.save()

    return redirect('profHome')
    return render(request, 'group/editGroup.html', {'group': group})