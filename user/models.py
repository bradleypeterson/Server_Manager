from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class AppUser(AbstractUser):
    ROLE = (
        ('faculty', 'faculty'),
        ('admin', 'admin'),
        ('student', 'student'),
    )
    role = models.CharField(max_length=100, choices=ROLE, default='faculty')

class CustomField(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

class Project(models.Model):
    # Date fields
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    # Basic info
    name = models.CharField(max_length=100)
    description = models.TextField()
    purpose = models.TextField()
    os = models.CharField(max_length=100)
    installed_software = models.TextField()
    tech_stack = models.TextField()
    # Array fields
    ip = models.GenericIPAddressField()
    issues = models.TextField()
    # Linked models
    custom_fields = models.ManyToManyField(CustomField)
    users = models.ManyToManyField(AppUser)
    # groups = models.ManyToManyField(Group, related_name='groups')
    def __str__(self):
        return self.name