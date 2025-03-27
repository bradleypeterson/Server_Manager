from django import forms
from .models import Group
from user.models import AppUser
from project.models import Project


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_name', 'description', 'users', 'projects']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['group_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Group Name'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter group description', 'rows': 3})
        self.fields['users'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['projects'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['users'].widget.attrs.update({'class': 'form-select'})
        self.fields['projects'].widget.attrs.update({'class': 'form-select'})