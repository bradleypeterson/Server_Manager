from django import forms
from group.models import Group
from users.models import User
from group.models import TestUser
from random import *
import string
import random


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['groupName', 'groupDescription', 'groupCredentials']

class TestUserForm(forms.ModelForm):
    class Meta:
        model = TestUser
        fields = ['firstname', 'lastname']
