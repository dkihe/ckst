from django import forms
from . import models

class NewEntry(forms.ModelForm):
    class Meta:
        model = models.UserData
        fields = ['account', 'account_password']
