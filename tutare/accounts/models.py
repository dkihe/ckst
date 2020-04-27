from django.db import models
from django.contrib.auth.models import User

# UserData model. Holds user-specific account/password entries, to be added by the user.
class UserData(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    account = models.CharField(max_length=25)
    account_password = models.CharField(max_length=25, default='')

    def __str__(self):
        return '{} / {} / {}'.format(self.user, self.account, self.account_password)
