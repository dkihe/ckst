from django.db import models


class User(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25, default='')

    def __str__(self):
        return '{} / {}'.format(self.username, self.password)

class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.CharField(max_length=25)
    account_password = models.CharField(max_length=25, default='')

    def __str__(self):
        return '{} / {}'.format(self.user, self.account, self.password)
