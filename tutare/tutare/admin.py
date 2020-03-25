from django.contrib import admin

from .models import ContactUs, UserAccount

admin.site.register(UserAccount)
admin.site.register(ContactUs)
