from typing import Union

from .constants import OPERATION_WITHDRAWAL, OPERATION_DEPOSIT, OPERATION_TRANSFERENCE
from .models import *


def get_transaction_object(_type, uuid) -> Union(Deposit, Transference, Withdrawal):
    """
    Returns object or raises ObjectDoesNotExists exception
    """
    if _type == OPERATION_DEPOSIT:
        operation = Deposit
    elif _type == OPERATION_TRANSFERENCE:
        operation = Transference
    elif _type == OPERATION_WITHDRAWAL:
        operation = Withdrawal
    else:
        # TODO raise error
        pass
    return operation.objects.get(uuid=uuid)
    