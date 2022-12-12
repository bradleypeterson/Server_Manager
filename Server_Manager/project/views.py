from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from .models import TestUser


def createProject(request, id):
    user = TestUser.objects.get(pk=id)

    if request.method == 'POST':
        form = ProjectForm(request.POST or None)
        if form.is_valid():
            try:
                instance = form.save(commit=False)
                instance.user = user
                instance.save()
                return redirect('studentHome', user.id)
            except:
                pass
    else:
        form = ProjectForm()
        return render(request, 'project/createProject.html', {'form': form, 'user': user})

# Create your views here.


def projectDetail(request, id):
    project = Project.objects.get(pk=id)

    context = {
        'project': project
    }
    return render(request, 'project/projectDetail.html', context)


def updateProject(request, id):
    project = Project.objects.get(pk=id)
    user = project.user
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('studentHome', user.id)
    return render(request, 'project/editProject.html', {'form': form, 'project': project})


def deleteProject(request, id):
    project = Project.objects.get(pk=id)
    user = project.user
    if request.method == 'POST':
        project.delete()
        return redirect('studentHome', user.id)
    return render(request, 'project/deleteProject.html', {'project':project})
