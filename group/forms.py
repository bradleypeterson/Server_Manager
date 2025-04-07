from django import forms
from .models import Group
from user.models import AppUser
from project.models import Project


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['group_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Group Name'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter group description', 'rows': 3})
        #self.fields['users'].widget.attrs.update({'class': 'form-check-input'})
        #self.fields['projects'].widget.attrs.update({'class': 'form-check-input'})
        #sself.fields['users'].widget.attrs.update({'class': 'form-select', 'multiple': 'multiple'})
        self.fields['available_users'] = forms.ModelMultipleChoiceField(
            queryset=AppUser.objects.all(),
            widget=forms.Select(attrs={'class': 'form-control'}),
            required=False
        )
        self.fields['available_projects'] = forms.ModelMultipleChoiceField(
            queryset=Project.objects.all(),
            widget=forms.Select(attrs={'class': 'form-control'}),
            required=False
        )

        #self.fields['projects'].widget.attrs.update({'class': 'form-select'})