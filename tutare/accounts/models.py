from django.db import models

# Create your models here.

class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.CharField(max_length=25)
    account_password = models.CharField(max_length=25, default='')

    def __str__(self):
        return '{} / {} / {}'.format(self.user, self.account, self.account_password)
