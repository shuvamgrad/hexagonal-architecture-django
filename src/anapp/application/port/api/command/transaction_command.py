from dataclasses import dataclass

from anapp.application.domain.model.identifier.transaction_id import TransactionId
from anapp.application.domain.model.identifier.user_id import UserId
from anapp.application.domain.model.amount import Amount

@dataclass
class TransactionCommand:
    transaction_id: TransactionId
    user_id: UserId
    amount: Amount
    