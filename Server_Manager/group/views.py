from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .models import Group
from users.models import User
from .forms import GroupForm, UserForm
from random import *
import string
import random


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

def generateUser(request):

    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('createPass')

    return render(request, 'group/credentials.html', {'form': form})

def createPass(request):
# generates random password successfully and
    char = string.ascii_letters + string.punctuation + string.digits
    password = " ".join(choice(char) for x in range(randint(5, 16)))

    context = {
        'pass': password
    }
    return render(request, 'group/displayPassword.html', context)

