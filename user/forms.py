from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'location', 'number_phone', 'picture']
