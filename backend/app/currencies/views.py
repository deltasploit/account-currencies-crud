from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status, generics

from .constants import STATUS_DELETED
from .models import Currency
from .serializers import CurrencySerializer


class CurrencyCreateView(generics.ListCreateAPIView):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.filter(~Q(status=STATUS_DELETED))


class CurrencyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()

    def delete(self, request, *args, **kwargs):
        currency = get_object_or_404(Currency, pk=kwargs['pk'])
        currency.status = STATUS_DELETED
        currency.save()
        return Response("Currency deleted", status=status.HTTP_204_NO_CONTENT)