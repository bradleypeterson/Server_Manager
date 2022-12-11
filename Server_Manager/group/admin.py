from django.contrib import admin
from .views import Group
from .models import Group, TestUser
# Register your models here.


admin.site.register(Group)
admin.site.register(TestUser)
