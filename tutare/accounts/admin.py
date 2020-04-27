from django.contrib import admin
from .models import UserData

# Registers the UserData model in the Admin site.
admin.site.register(UserData)
