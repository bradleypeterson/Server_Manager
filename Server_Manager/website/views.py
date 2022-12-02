from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from courses.models import Course
from project.models import Project
from group.models import Group
from user.models import AppUser

def login(request):
    return render(request, "website/login.html")

def profHome(request, id):
    user = get_object_or_404(AppUser, pk=id)
    return render(request, "website/professorHome.html", {"courses": Course.objects.filter(user__pk=id)})

def studentHome(request):
    return render(request, "website/studentHome.html", {"projects": Project.objects.all()})