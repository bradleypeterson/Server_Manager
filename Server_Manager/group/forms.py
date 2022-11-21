from django import forms
from group.models import Group
from users.models import User
from random import *
import string
import random


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = "__all__"

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'useraccesslevel')
