from .constants import *

from django.db import models


# Create your models here.
class Currency(models.Model):
    name = models.CharField(max_length=50)  # Bitcoin
    description = models.TextField(blank=True)
    short_id = models.CharField(max_length=10)  # BTC
    status = models.CharField(max_length=20, choices=CURRENCY_STATUS, default=STATUS_ACTIVE)
    # Other fields, icons, currency type (flat, cripto), config fields (available for futures, etc)

    def is_transactionable(self):
        return self.status == STATUS_ACTIVE
        