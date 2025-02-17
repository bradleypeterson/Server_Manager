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

from website.views import login
from website.views import profHome

from user import views as user_views

app_name = 'servermanager'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('professorHome/<int:id>', profHome, name="profHome"),
   # path('', login),
    path('', user_views.login_user, name="login"),
    path('register/', user_views.register, name="register"),
    path('resetPassword/', user_views.password_reset, name="resetPassword"),
    path('user/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
