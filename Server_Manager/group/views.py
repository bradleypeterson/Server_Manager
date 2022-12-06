from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.hashers import make_password
from .models import Course
from .models import Group
from user.models import AppUser
from .forms import GroupForm, UserForm
from random import *
import string
import random


# Create your views here.
def createGroup(request, id):
    course = Course.objects.get(pk=id)
    user = course.user
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            try:
                instance = form.save(commit=False)
                instance.course = course;
                instance.save()
                return redirect('profHome', user.id)
            except:
                pass
    else:
        form = GroupForm()
        return render(request, 'group/createGroup.html', {'form': form, 'course': course})


def groupDetail(request, id):
    group = get_object_or_404(Group, pk=id)
    groupId = id
    user = AppUser.objects.filter(group__pk=id)
    context = {"group": group, "user": user, "groupId": groupId}
    return render(request, "group/groupDetail.html", context=context)


def destroyGroup(request, id):
    group = Group.objects.get(id=id)
    course = group.course
    user = course.user
    group.delete()
    return redirect('profHome', user.id)


def editGroup(request, id):
    group = get_object_or_404(Group, pk=id)
    return render(request, "group/editGroup.html", {"group": group})


def updateGroup(request, id):
    group = Group.objects.get(id=id)
    course = group.user
    user = course.user

    form = GroupForm(request.POST, instance=group)
    if form.is_valid():
        form.save()

    return redirect('profHome', user.id)
    return render(request, 'group/editGroup.html', {'group': group})


def generateUser(request, id):
    group = Group.objects.get(pk=id)
    char = string.ascii_letters + string.punctuation + string.digits
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                instance = form.save(commit=False)
                username = instance.first_name + instance.last_name
                instance.username = instance.first_name + instance.last_name
                password = "".join(choice(char) for x in range(randint(8, 16)))
                instance.password = make_password(password)
                instance.group = group
                instance.save()
                context = {"pass": password, "user": username}
                context['group'] = group
                return render(request, "group/displayPassword.html", context=context)
            except:
                pass
    else:
        form = UserForm()
        return render(request, 'group/createCredentials.html', {'form': form, 'group': group})

def deleteCredentials(request, id):
  user = AppUser.objects.get(id=id)
  user.delete()
  return redirect('groupDetail', user.group.id)

