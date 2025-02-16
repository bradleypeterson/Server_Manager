from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from user.models import AppUser
def login(request):
    return render(request, "website/login.html")

def profHome(request, id):
    user = get_object_or_404(AppUser, pk=id)
    return render(request, "website/professorHome.html", {})