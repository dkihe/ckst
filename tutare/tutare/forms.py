from django import forms
from .models import User, ContactUs


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['password']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'phone', 'message')
