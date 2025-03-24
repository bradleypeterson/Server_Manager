from django.forms.models import ModelForm

from project.models import Project
from project.models import Server

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'stack', 'last_audit', 'currently_in_use', 'repo_link', 'trello_link', 'notes', 'description', 'users', 'groups']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['stack'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_audit'].widget.attrs.update({'class': 'form-control'})
        self.fields['currently_in_use'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['repo_link'].widget.attrs.update({'class': 'form-control'})
        self.fields['trello_link'].widget.attrs.update({'class': 'form-control'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['users'].widget.attrs.update({'class': 'form-control'})
        self.fields['groups'].widget.attrs.update({'class': 'form-control'})

class ServerForm(ModelForm):
    class Meta:
        model = Server
        #fields = ['name', 'operating_system', 'ip_address', 'software_installed', 'idrac_info', 'notes', 'description', 'project', 'created_by']
        fields = ['name', 'operating_system', 'ip_address', 'software_installed', 'idrac_info', 'notes', 'description', 'created_by']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['operating_system'].widget.attrs.update({'class': 'form-control'})
        self.fields['ip_address'].widget.attrs.update({'class': 'form-control'})
        self.fields['software_installed'].widget.attrs.update({'class': 'form-control'})
        self.fields['idrac_info'].widget.attrs.update({'class': 'form-control'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        #self.fields['project'].widget.attrs.update({'class': 'form-control'})
        self.fields['created_by'].widget.attrs.update({'class': 'form-control'})
