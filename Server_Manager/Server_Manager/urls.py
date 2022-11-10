"""Server_Manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from website.views import login
from website.views import profHome, studentHome
from courses.views import detail
from courses.views import editProf
from courses.views import createCourse
from courses.views import destroy
from courses.views import update
from project.views import *
from group.views import *

from users import views as user_views

app_name = 'servermanager'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('createCourse', createCourse, name="createProf"),
    path('', login),
    path('professorHome/', profHome, name="profHome"),
    path('courses/<int:id>', detail, name="detail"),
    path('edit/<int:id>', editProf, name="editProf"),
    path('delete/<int:id>', destroy, name="deleteProf"),
    path('update/<int:id>', update, name="updateProf"),
    path('register/', user_views.register, name="register"),

    path('createGroup', createGroup, name="createGroup"),
    path('group/<int:id>', groupDetail, name="groupDetail"),
    path('updateGroup/<int:id>', updateGroup, name="updateGroup"),
    path('deleteGroup/<int:id>', destroyGroup, name="deleteGroup"),
    path('editGroup/<int:id>', editGroup, name="editGroup"),
    path('generateUser', generateUser, name="generateUser"),
    path('createPass', createPass, name="createPass"),

    path('studentHome/', studentHome, name="studentHome"),
    path('projects/<int:id>', projectDetail, name="projectDetail"),
    path('createproject', createProject, name='createProject'),
    path('deleteproject/<int:id>', deleteProject, name="deleteProject"),
    path('updateproject/<int:id>', updateProject, name="updateProject"),

]
