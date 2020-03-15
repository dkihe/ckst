from django.db import models


class User(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25, default='')

    def __str__(self):
        return '{} / {}'.format(self.username, self.password)
