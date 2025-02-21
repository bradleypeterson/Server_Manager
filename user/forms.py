from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from user.models import AppUser


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'First Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'width: 300px;', 'class': 'form-control'}))
    password1 = forms.CharField(
        help_text='Enter Password',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'style': 'width: 300px;'}),
    )
    password2 = forms.CharField(
        help_text='Confirm Password',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'style': 'width: 300px;'}),
    )

    class Meta:
        model = AppUser
        fields = ("username",)

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'width: 300px;', 'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 300px;', 'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = AppUser.objects.filter(username=username)
        return username

    class Meta:
        model = AppUser
        fields = ("username",)

class ResetPasswordForm(PasswordResetForm):
    password1 = forms.CharField(
        help_text='Enter Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password', 'style': 'width: 300px;'}),
    )

    password2 = forms.CharField(
        help_text='Confirm Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'style': 'width: 300px;'}),
    )