from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["projecttitle", 'projectdescription', 'dockerid',
                  'projectlanguage', 'projectdatabase', 'projectbackend',
                  'projecttechnologymisc', 'projectlink', 'projectimagelink',
                  'addeddate', 'updateddate']
