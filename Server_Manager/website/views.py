from django.http import HttpResponse
from django.shortcuts import render
from courses.models import Course
from project.models import Project
from group.models import Group

def login(request):
    return render(request, "website/login.html")

def profHome(request):
    return render(request, "website/professorHome.html", {"courses": Course.objects.all()})

def studentHome(request):
    return render(request, "website/studentHome.html", {"projects": Project.objects.all()})