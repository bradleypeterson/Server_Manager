from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["project_title", 'project_description', 'docker_id',
                  'project_language', 'project_database', 'project_backend',
                  'project_technology_misc', 'project_link', 'project_image_link',
                  'added_date', 'updated_date']
