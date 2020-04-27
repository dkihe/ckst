from django import forms
from . import models

# NewEntry form. Allows users to enter new account+password entries in the database.
class NewEntry(forms.ModelForm):
    class Meta:
        model = models.UserData
        fields = ['account', 'account_password']
