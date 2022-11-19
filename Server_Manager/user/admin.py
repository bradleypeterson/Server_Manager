from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AppUser
from .forms import RegistrationForm


class CustomUserAdmin(UserAdmin):
    add_form = RegistrationForm
    form = RegistrationForm
    model = AppUser

    fieldsets = (
        (None, {'fields': ('username', 'password',)}),
        ('Personal info', {'fields': ('role',)}),
        ('Permissions', {'fields': ()}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'role',),
        }),
    )


admin.site.register(AppUser, CustomUserAdmin)