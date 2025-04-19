from django.forms.models import ModelForm
from django import forms
from project.models import Project
from project.models import Server
from user.models import AppUser
from group.models import Group

#Project Form Fields
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'stack', 'last_audit', 'currently_in_use', 'repo_link', 'trello_link', 'notes', 'description']

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
        # self.fields['users'].widget.attrs.update({'class': 'form-select'})
        # self.fields['groups'].widget.attrs.update({'class': 'form-select'})

        if self.instance.pk is None:
            self.fields['available_users'] = forms.ModelMultipleChoiceField(
                queryset=AppUser.objects.all(),
                widget=forms.Select(attrs={'class': 'form-control'}),
                required=False
            )
            self.fields['available_groups'] = forms.ModelMultipleChoiceField(
                queryset=Group.objects.all(),
                widget=forms.Select(attrs={'class': 'form-control'}),
                required=False
            )
            self.fields['selected_users'] = forms.ModelMultipleChoiceField(
                queryset=AppUser.objects.none(),
                widget=forms.Select(attrs={'class': 'form-control'}),
                required=False
            )
            self.fields['selected_groups'] = forms.ModelMultipleChoiceField(
                queryset=Group.objects.none(),
                widget=forms.Select(attrs={'class': 'form-control'}),
                required=False
            )
        else:
            project = Project.objects.get(pk=self.instance.pk)

            user_pks = project.users.values_list('id', flat=True)
            group_pks = project.groups.values_list('id', flat=True)

            self.fields['selected_users'] = forms.ModelMultipleChoiceField(
                queryset=AppUser.objects.filter(id__in=user_pks),
                widget=forms.Select(attrs={'class': 'form-control'}),
                required=False
            )
            self.fields['selected_groups'] = forms.ModelMultipleChoiceField(
                queryset=Group.objects.filter(id__in=group_pks),
                widget=forms.Select(attrs={'class': 'form-control'}),
                required=False
            )
            self.fields['available_users'] = forms.ModelMultipleChoiceField(
                queryset=AppUser.objects.exclude(id__in=user_pks),
                widget=forms.Select(attrs={'class': 'form-control'}),
                required=False
            )
            self.fields['available_groups'] = forms.ModelMultipleChoiceField(
                queryset=Group.objects.exclude(id__in=group_pks),
                widget=forms.Select(attrs={'class': 'form-control'}),
                required=False
            )

#Server Form fields
class ServerForm(ModelForm):
    class Meta:
        model = Server
        fields = ['name', 'operating_system', 'ip_address', 'software_installed', 'idrac_info', 'notes', 'description', 'project']
        #fields = ['name', 'operating_system', 'ip_address', 'software_installed', 'idrac_info', 'notes', 'description', 'created_by']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'tab-index': '1'})
        self.fields['operating_system'].widget.attrs.update({'class': 'form-select', 'tab-index': '3', 'rows': '2'})
        self.fields['ip_address'].widget.attrs.update({'class': 'form-control', 'tab-index': '2'})
        self.fields['software_installed'].widget.attrs.update({'class': 'form-control', 'tab-index': '5', 'rows': '2' })
        self.fields['idrac_info'].widget.attrs.update({'class': 'form-control', 'tab-index': '4', 'rows': '4'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control', 'tab-index': '6', 'rows': '3'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'tab-index': '7', 'rows': '4'})
        self.fields['project'].widget.attrs.update({'class': 'form-select', 'tab-index': '8'})
