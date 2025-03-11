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

# class Project(models.Model):
#     # Date fields
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#     # Basic info
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     purpose = models.TextField()
#     installed_software = models.TextField()
#     tech_stack = models.TextField()
#     # Array fields
#     ip = models.GenericIPAddressField()
#     issues = models.TextField()
#     # Linked models
#     custom_fields = models.ManyToManyField(CustomField)
#     users = models.ManyToManyField(AppUser)
#     # groups = models.ManyToManyField(Group, related_name='groups')
#     def __str__(self):
#         return self.name

class Server(models.Model):
    # Date fields
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    # Basic info
    name = models.CharField(max_length=100)
    operating_system = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    software_installed = models.TextField(blank=True, null=True)
    idrac_info = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # Linked models
    custom_fields = models.ManyToManyField(CustomField)
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True, blank=True, related_name='server_projects')
    created_by = models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    # Fields for the project
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    stack = models.TextField(blank=True, null=True)
    user_rights = models.TextField(blank=True, null=True)
    last_audit = models.DateField(blank=True, null=True)
    currently_in_use = models.BooleanField(default=True)
    github_repo_link = models.URLField(blank=True, null=True)
    trello_link = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # Linked models
    custom_fields = models.ManyToManyField(CustomField)
    users = models.ManyToManyField(AppUser)
    servers = models.ManyToManyField(Server, related_name='projects')  # keep 'projects' as the related_name

    def __str__(self):
        return self.name