from django.db import models
from django.contrib.auth.models import User

class ContactUs(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Contact Us"


class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.CharField(max_length=25)
    account_password = models.CharField(max_length=25, default='')

    def __str__(self):
        return '{} / {}'.format(self.account, self.account_password)
