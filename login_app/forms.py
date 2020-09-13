from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

# sign up form
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'username'}) 
    )
    email = forms.EmailField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'user@domain.com'}) 
    )
    password1 = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'password'}) 
    )
    password2 = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 're-enter the password'}) 
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'username'}) 
    )
    password = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'password'}) 
    )
    class Meta:
        model = User
        fields = ['username', 'password']

# edit profile form
class EditProfile(forms.ModelForm):
    fullname = forms.CharField(
        required=False,
        label="Full name",
    )
    class Meta:
        model = Profile
        exclude = ['user']