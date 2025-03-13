from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View

from project.forms import ProjectForm

# Create your views here.
@login_required
def add_project(request):
    form = ProjectForm(request.POST or None)
    return render(request, "addProject.html", {})


class AddProjectView(View):
    def get(self, request):
        form = ProjectForm(request.POST or None)
        return render(request, "addProject.html", {'form': form})
    def post(self, request):
        form = ProjectForm(request.POST or None)
        print(form.is_valid())
        form.save()
        return render(request, "addProject.html", {'form': form})
