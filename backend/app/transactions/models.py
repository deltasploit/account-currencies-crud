import uuid

from django.db import models

from .constants import LOG_TYPES, OPERATION_TYPES
from currencies.models import Currency
from users.models import UserAccount


class TransactionLog(models.Model):
    created = models.DateTimeField()
    account = models.ForeignKey(UserAccount, related_name='logs', on_delete=models.CASCADE)
    operation_type = models.CharField(max_length=30, choices=OPERATION_TYPES)
    event = models.CharField(max_length=50, choices=LOG_TYPES)
    uuid = models.CharField(max_length=100, default=uuid.uuid4, editable=False, unique=True)
    additional_info = models.TextField(blank=True)


class Transference(models.Model):
    created = models.DateTimeField()
    sender = models.ForeignKey(UserAccount, related_name='sent_transferences', on_delete=models.PROTECT)
    receiver = models.ForeignKey(UserAccount, related_name='received_transferences', on_delete=models.PROTECT)
    amount = models.FloatField()
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    uuid = models.CharField(max_length=100, default=uuid.uuid4, editable=False, unique=True)


class Deposit(models.Model):
    created = models.DateTimeField()
    account = models.ForeignKey(UserAccount, related_name='received_deposits', on_delete=models.PROTECT)
    amount = models.FloatField()
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    uuid = models.CharField(max_length=100, default=uuid.uuid4, editable=False, unique=True)


class Withdrawal(models.Model):
    created = models.DateTimeField()
    account = models.ForeignKey(UserAccount, related_name='withdrawals', on_delete=models.PROTECT)
    amount = models.FloatField()
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    uuid = models.CharField(max_length=100, default=uuid.uuid4, editable=False, unique=True)
