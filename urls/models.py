from django.db import models

from users.models import Account


class Url(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT,
                                related_name='url_account')
    link = models.URLField()
    status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.link}, {self.status}, {self.account}'

