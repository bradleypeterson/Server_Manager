from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AppUser

class CustomUserAdmin(UserAdmin):
    model = AppUser

    fieldsets = (
        ('Personal info', {'fields': ('first_name', 'last_name', 'username', 'password', 'is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )


admin.site.register(AppUser, CustomUserAdmin)