from django.http import HttpResponse
from django.shortcuts import render
from courses.models import Course

# User Login
def login(request):
    return render(request, "website/login.html")

#Professor home
def profHome(request):
    return render(request, "website/professorHome.html",
    {"courses": Course.objects.all()})


