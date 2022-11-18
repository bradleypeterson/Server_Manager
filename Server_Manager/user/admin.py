from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AppUser

admin.site.register(AppUser, UserAdmin)