from django.contrib import admin

from .models import User
from .models import UserAccount

admin.site.register(User)
admin.site.register(UserAccount)
