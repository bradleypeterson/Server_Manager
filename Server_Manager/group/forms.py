from django import forms
from django.contrib.auth.forms import AuthenticationForm
from group.models import Group
from group.models import TestUser


from random import *
import string
import random

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['groupName', 'groupDescription']

class TestUserForm(forms.ModelForm):
    class Meta:
        model = TestUser
        fields = ['firstname', 'lastname']


class StudentLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'width: 300px;', 'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 300px;', 'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = TestUser.objects.filter(username=username)
        return username

    class Meta:
        model = TestUser
        fields = ("username", "password")

