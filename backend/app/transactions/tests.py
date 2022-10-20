from django.test import TestCase

from .models import *
from currencies.models import Currency
from currencies.constants import STATUS_ACTIVE
from users.models import UserAccount
from django.contrib.auth.models import User


class TransactionsTestCase(TestCase):
    def setUp(self) -> None:
        # Create users and user accounts
        user1 = User.objects.create(username='user1', password='pass')
        user2 = User.objects.create(username='user2', password='pass')
        ua_1 = UserAccount.objects.create(user=user1, alias='user1-alias')
        ua_2 = UserAccount.objects.create(user=user2, alias='user2-alias')
        c1 = Currency.objects.create(name='Bitcoin', short_id='BTC', status=STATUS_ACTIVE)

    def test_deposit_withdrawal_get_balance(self):
        ua = UserAccount.objects.get(alias='user1-alias')
        c = Currency.objects.get(short_id='BTC')
        # First balance
        self.assertEqual(ua.get_balance(c), 0)
        # Recurrent deposits
        ua.deposit(100, c)
        self.assertEqual(ua.get_balance(c), 100)
        ua.deposit(200, c)
        self.assertEqual(ua.get_balance(c), 300)
        # Withdrawal
        ua.withdraw(50, c)
        self.assertEqual(ua.get_balance(c), 250)
        # TODO assert exception when insufficient funds

    def test_transference(self):
        ua_sender = UserAccount.objects.get(alias='user1-alias')
        ua_receiver = UserAccount.objects.get(alias='user2-alias')
        c = Currency.objects.get(short_id='BTC')
        # TODO assert exception when insufficient funds
        # TODO assert exception when transfering negative and zero
        ua_sender.deposit(100, c)
        ua_sender.transfer(ua_receiver, 25, c)
        self.assertEqual(ua_sender.get_balance(c), 75)
        self.assertEqual(ua_receiver.get_balance(c), 25)

