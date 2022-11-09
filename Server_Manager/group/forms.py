from django import forms
from group.models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = "__all__"
