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
from django.conf import settings
import user.views as user_views
import group.views as group_views
import project.views as project_views

app_name = 'servermanager'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', user_views.home, name="home"),
    path('register/', user_views.RegisterView.as_view(), name="register"),
    path('resetPassword/<int:user_id>/', user_views.password_reset, name="resetPassword"),
    path('addProject/', project_views.AddProjectView.as_view(), name="addProject"),
    path('addServer/', project_views.AddServerView.as_view(), name="addServer"),
    path('server/<int:server_id>/', user_views.viewServer, name="viewServer"),
    path('project/<int:project_id>/', user_views.viewProject, name="viewProject"),
    path('', user_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('group/', group_views.CreateGroupView.as_view(), name="group"),
    path('group/list/', group_views.groupList, name='group_list'),
    path('pingServer/', user_views.ping_server, name="pingServer"),
    path('delete-project/<int:project_id>/', project_views.delete_project, name='delete_project'),
    path('delete-server/<int:server_id>/', project_views.delete_server, name='delete_server'),
    path('delete-group/<int:group_id>/', project_views.delete_group, name='delete_group')
]
