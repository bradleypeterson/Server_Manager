from django.contrib import admin
from .models import Group
from django.contrib.auth.models import Group as DjangoGroup

# Register your models here.

admin.site.register(Group)
admin.site.unregister(DjangoGroup)