from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

def createProject(request):
    form = ProjectForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('studentHome')

    return render(request, 'project/createProject.html', {'form': form})

# Create your views here.


def projectDetail(request, id):
    project = Project.objects.get(pk=id)
    context = {
        'project': project
    }
    return render(request, 'project/projectDetail.html', context)


def updateProject(request, id):
    project = Project.objects.get(pk=id)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('studentHome')
    return render(request, 'project/editProject.html', {'form': form, 'project':project})


def deleteProject(request, id):
    project = Project.objects.get(pk=id)
    if request.method == 'POST':
        project.delete()
        return redirect('studentHome')
    return render(request, 'project/deleteProject.html', {'project':project})
