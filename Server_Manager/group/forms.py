from django import forms
from group.models import Group
from user.models import AppUser
from random import *
import string
import random

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['groupName', 'groupDescription']

class UserForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ['first_name', 'last_name']

