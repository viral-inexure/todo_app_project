from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import Profile, Todo, Category
from django import forms
from django.contrib.admin.widgets import AdminDateWidget


class LoginForm(AuthenticationForm):
    username = UsernameField(label='Email / Username')

    class Meta:
        model = Profile
        fields = ['username', 'password']


class RegistrationForm(forms.Form):
    mobile_number = forms.IntegerField()
    email = forms.EmailField()
    date = forms.DateField(widget=AdminDateWidget())

    class Meta:
        model = Profile
        fields = ['mobile_number', 'email', 'date']
