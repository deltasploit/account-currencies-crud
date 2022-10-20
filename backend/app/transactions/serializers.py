from rest_framework import serializers

from .models import *


class TransactionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionLog
        fields = '__all__'


class TransferenceSerializer(serializers.ModelSerializer):
    """Serializer object to be used when doing a transference"""
    class Meta:
        model = Transference
        exclude = ['created', 'sender', 'uuid']


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'


class WithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdrawal
        fields = '__all__'
