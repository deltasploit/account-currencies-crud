from locale import currency
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *

from currencies.models import Currency
from users.models import UserAccount

# Create your views here.
class Transference_APIView(APIView):
    def post(self, request):
        serializer = TransferenceSerializer(data=request.data)
        if serializer.is_valid():
            # TODO get sender user account
            sender_account = request.user
            receiver_account_alias = request.POST["receiver"]
            amount = request.POST["amount"]
            currency_short_id = request.POST["currency"]
            currency = Currency.objects.get(currency_short_id)
            receiver_account = UserAccount.objects.get(receiver_account_alias)
            # TODO handle ObjectDoesNotExists and return "User not found error"
            sender_account.transfer(
                receiver_account, 
                amount,
                currency
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # It's possible to implement, for example, get method for get more details about transference


class Deposit_APIView(APIView):
    def post(self, request):
        serializer = DepositSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # It's possible to implement, for example, get method for get more details about transference


class Withdrawal_APIView(APIView):
    def post(self, request):
        serializer = WithdrawalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # It's possible to implement, for example, get method for get more details about transference
