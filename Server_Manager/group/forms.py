from django import forms
from group.models import Group
from user.models import AppUser
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
