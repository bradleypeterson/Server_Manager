from django import forms
from .models import Group
from user.models import AppUser
from project.models import Project

#Fields for Group Form
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['group_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Group Name'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter group description', 'rows': 3})

        if self.instance.pk is None:
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
            self.fields['selected_users'] = forms.ModelMultipleChoiceField(
                queryset=AppUser.objects.none(),
                widget=forms.Select(attrs={'class': 'form-control'}),
                required=False
            )
            self.fields['selected_projects'] = forms.ModelMultipleChoiceField(
                queryset=Project.objects.none(),
                widget=forms.Select(attrs={'class': 'form-control'}),
                required=False
            )
        else:
            group = Group.objects.get(pk=self.instance.pk)

            user_pks = group.users.values_list('id', flat=True)
            project_pks = Project.objects.filter(groups=group).values_list('id', flat=True)

            self.fields['selected_users'] = forms.ModelMultipleChoiceField(
                queryset=AppUser.objects.filter(id__in=user_pks),
                widget=forms.Select(attrs={'class': 'form-control'}),
                required=False
            )
            self.fields['selected_projects'] = forms.ModelMultipleChoiceField(
                queryset=Project.objects.filter(id__in=project_pks),
                widget=forms.Select(attrs={'class': 'form-control'}),
                required=False
            )
            self.fields['available_users'] = forms.ModelMultipleChoiceField(
                queryset=AppUser.objects.exclude(id__in=user_pks),
                widget=forms.Select(attrs={'class': 'form-control'}),
                required=False
            )
            self.fields['available_projects'] = forms.ModelMultipleChoiceField(
                queryset=Project.objects.exclude(id__in=project_pks),
                widget=forms.Select(attrs={'class': 'form-control'}),
                required=False
            )