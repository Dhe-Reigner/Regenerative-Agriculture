from django import forms
from django.forms import ModelForm
from .models import RegisterUser

class RegisterUserForm(ModelForm):
    class Meta:
        model = RegisterUser
        fields = ('name','email','username','password')