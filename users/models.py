from django.contrib.auth.models import User
from django.db import models

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='account')
    username = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.username
