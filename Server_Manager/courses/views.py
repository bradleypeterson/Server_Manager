from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from courses.forms import CourseForm

# See course detail
def detail(request, id):
    course = get_object_or_404(Course, pk=id)
    return render(request, "courses/detail.html", {"course": course})

# Professor can edit a course
def editProf(request, id):
    course = get_object_or_404(Course, pk=id)
    return render(request, "courses/edit.html", {"course": course})

# Professor can create a course
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

# Professor can delete a course
def destroy(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('profHome')

# Professor can update a course
def update(request, id):
    course = Course.objects.get(id=id)
    form = CourseForm(request.POST, instance=course)
    if form.is_valid():
        form.save()
        return redirect('profHome')
    return render(request, 'courses/editCourse.html', {'course': course})
