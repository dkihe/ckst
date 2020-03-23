from django.contrib import admin

from .models import User, ContactUs

admin.site.register(User)
admin.site.register(ContactUs)