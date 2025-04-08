from django.db import models

class OperatingSystem(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# Create your models here.
class Project(models.Model):
    # Fields for the project
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    stack = models.TextField(blank=True, null=True)
    last_audit = models.DateField(blank=True, null=True)
    currently_in_use = models.BooleanField(default=True)
    repo_link =  models.URLField(blank=True, null=True)
    trello_link = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # Linked models
    users = models.ManyToManyField('user.AppUser', related_name='project_users', blank=True)
    groups = models.ManyToManyField('group.Group', related_name='project_groups', blank=True)
    created_by = models.ForeignKey('user.AppUser', on_delete=models.SET_NULL, null=True, blank=True, related_name='project_created_by')
    updated_by = models.ForeignKey('user.AppUser', on_delete=models.SET_NULL, null=True, blank=True, related_name='project_updated_by')

    def __str__(self):
        return self.name

class Server(models.Model):
    # Date fields
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    # Basic info
    name = models.CharField(max_length=100)
    operating_system = models.ForeignKey('OperatingSystem', on_delete=models.SET_NULL, null=True, blank=True, related_name='server_operating_system')
    ip_address = models.GenericIPAddressField()
    software_installed = models.TextField(blank=True, null=True)
    idrac_info = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # Linked models
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True, blank=True, related_name='server_projects')
    created_by = models.ForeignKey('user.AppUser', on_delete=models.SET_NULL, null=True, blank=True, related_name='server_created_by')
    updated_by = models.ForeignKey('user.AppUser', on_delete=models.SET_NULL, null=True, blank=True, related_name='server_updated_by')

    def __str__(self):
        return self.name
