from django import forms
from .models import Group
from user.models import AppUser
from project.models import Project

class GroupForm(forms.ModelForm):
    group_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Group Name', 'style': 'width: 300px;', 'class': 'form-control'})
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter group description', 'rows': 3, 'class': 'form-control'})
    )

    users = forms.ModelMultipleChoiceField(
        queryset=AppUser.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )

    projects = forms.ModelMultipleChoiceField(
        queryset=Project.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )

    class Meta:
        model = Group
        fields = ['group_name', 'description', 'users', 'projects']
