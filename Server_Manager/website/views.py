from django.http import HttpResponse
from django.shortcuts import render
from courses.models import Course

def login(request):
    return render(request, "website/login.html")

def profHome(request):
    return render(request, "website/professorHome.html",
    {"courses": Course.objects.all()})


from courses.models import Course