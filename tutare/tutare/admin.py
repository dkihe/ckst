from django.contrib import admin

from .models import User, ContactUs, UserAccount

admin.site.register(User)
admin.site.register(UserAccount)
admin.site.register(ContactUs)
