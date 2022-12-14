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
from django.contrib.auth import views as auth_views
from django.urls import path

import group.views
from website.views import login
from website.views import profHome, studentHome
from courses.views import detail
from courses.views import editProf
from courses.views import createCourse
from courses.views import destroy
from courses.views import update
from project.views import createProject, updateProject, projectDetail, deleteProject
from group.views import *

from user import views as user_views

app_name = 'servermanager'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('createCourse/<int:id>', createCourse, name="createProf"),
    path('professorHome/<int:id>', profHome, name="profHome"),
   # path('', login),
    path('', user_views.login_user, name="login"),
    path('studentLogin/', studentLogin, name='studentLogin'),


    path('courses/<int:id>', detail, name="detail"),
    path('edit/<int:id>', editProf, name="editProf"),
    path('delete/<int:id>', destroy, name="deleteProf"),
    path('update/<int:id>', update, name="updateProf"),
    path('register/', user_views.register, name="register"),

    path('createGroup/<int:id>', createGroup, name="createGroup"),
    path('group/<int:id>', groupDetail, name="groupDetail"),
    path('profProjects/<int:id>', profProjects, name="profProjects"),
    path('updateGroup/<int:id>', updateGroup, name="updateGroup"),
    path('deleteGroup/<int:id>', destroyGroup, name="deleteGroup"),
    path('editGroup/<int:id>', editGroup, name="editGroup"),
    #path('generateUser', generateUser, name="generateUser"),
    #path('createPass', createPass, name="createPass"),
    path('createCredentials/<int:id>', generateUser, name="generateUser"),
    path('group/deleteCredentials/<int:id>', deleteCredentials, name="deleteCredentials"),

    path('user/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),


    path('studentHome/<int:id>', studentHome, name="studentHome"),
    path('projects/<int:id>', projectDetail, name="projectDetail"),
    path('createproject/<int:id>', createProject, name='createProject'),
    path('deleteproject/<int:id>', deleteProject, name="deleteProject"),
    path('updateproject/<int:id>', updateProject, name="updateProject"),
    path('studentLogin', studentLogin, name="studentLogin"),

]
