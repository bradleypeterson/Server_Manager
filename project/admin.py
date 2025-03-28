from django.contrib import admin
from .models import Project, OperatingSystem, Server

admin.site.register(Project)
admin.site.register(OperatingSystem)
admin.site.register(Server)
