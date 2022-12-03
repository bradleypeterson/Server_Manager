from django.shortcuts import render, get_object_or_404, redirect

from group.models import Group
from .models import Course

from courses.forms import CourseForm


def detail(request, id):
    course = get_object_or_404(Course, pk=id)
    courseId = id
    list_group = Group.objects.filter(course__pk=id)
    context = { "course": course, "group": list_group, "courseId": courseId}
    return render(request, "courses/detail.html", context=context)


def editProf(request, id):
    course = get_object_or_404(Course, pk=id)
    return render(request, "courses/edit.html", {"course": course})


def createCourse(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('profHome')
            except:
                pass
    else:
        form = CourseForm()
        return render(request, 'courses/createCourse.html', {'form': form})


def destroy(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('profHome')


def update(request, id):
    course = Course.objects.get(id=id)
    form = CourseForm(request.POST, instance=course)
    if form.is_valid():
        form.save()
        return redirect('profHome')
    return render(request, 'courses/editCourse.html', {'course': course})
