from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AppUser

class CustomUserAdmin(UserAdmin):
    model = AppUser

    fieldsets = (
        ('Personal info', {'fields': ('first_name', 'last_name', 'username', 'password')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'password1', 'password2'),
        }),
    )


admin.site.register(AppUser, CustomUserAdmin)