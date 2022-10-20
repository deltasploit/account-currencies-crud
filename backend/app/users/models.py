from datetime import datetime
from django.db import models, transaction
from django.contrib.auth.models import User

from transactions.constants import *


# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alias = models.CharField(max_length=30, unique=True)

    def __str__(self) -> str:
        return f"{self.user.username} - account"

    def get_received_money(self, currency) -> int:
        received_transactions = self.received_transferences.filter(currency=currency).aggregate(models.Sum('amount'))['amount__sum'] or 0
        received_deposits = self.received_deposits.filter(currency=currency).aggregate(models.Sum('amount'))['amount__sum'] or 0
        return received_deposits + received_transactions

    def get_sent_money(self, currency) -> int:
        sent_transactions = self.sent_transferences.all().aggregate(models.Sum('amount'))['amount__sum'] or 0
        withdrawals = self.withdrawals.filter(currency=currency).aggregate(models.Sum('amount'))['amount__sum'] or 0
        return sent_transactions + withdrawals
    
    def get_balance(self, currency) -> int:
        return self.get_received_money(currency) - self.get_sent_money(currency)

    def transfer(self, receiver, amount, currency):
        from transactions.models import Transference, TransactionLog
        timestamp = datetime.now()
        if not currency.is_transactionable:
            # Raise exception
            pass
        with transaction.atomic():
            if self.get_balance(currency) < amount:
                # Raise exception
                pass
            transference = Transference.objects.create(
                created=timestamp,
                sender=self,
                receiver=receiver,
                amount=amount,
                currency=currency
            )
            transference_log = TransactionLog.objects.create(
                created=timestamp,
                account=self,
                operation_type=OPERATION_TRANSFERENCE,
                event=LOG_TRANSFERENCE_SENT_OK
            )
            transference_log_received = TransactionLog.objects.create(
                created=timestamp,
                account=receiver,
                operation_type=OPERATION_TRANSFERENCE,
                event=LOG_TRANSFERENCE_RECEIVED_OK
            )
        return transference

    def deposit(self, amount, currency):
        from transactions.models import Deposit, TransactionLog
        timestamp = datetime.now()
        if not currency.is_transactionable:
            # Raise exception
            pass
        with transaction.atomic():
            deposit = Deposit.objects.create(
                created=timestamp,
                account=self,
                amount=amount,
                currency=currency
            )
            deposit_log = TransactionLog.objects.create(
                created=timestamp,
                account=self,
                operation_type=OPERATION_DEPOSIT,
                event=LOG_DEPOSIT_OK    
            )
        return deposit

    def withdraw(self, amount, currency):
        from transactions.models import Withdrawal, TransactionLog
        timestamp = datetime.now()
        if not currency.is_transactionable:
            # Raise exception
            pass
        with transaction.atomic():
            if self.get_balance(currency) < amount:
                # Raise exception
                pass
            withdrawal = Withdrawal.objects.create(
                created=timestamp,
                account=self,
                amount=amount,
                currency=currency
            )
            withdraw_log = TransactionLog.objects.create(
                created=timestamp,
                account=self,
                operation_type=OPERATION_WITHDRAWAL,
                event=LOG_WITHDRAWAL_OK    
            )
        return withdrawal
