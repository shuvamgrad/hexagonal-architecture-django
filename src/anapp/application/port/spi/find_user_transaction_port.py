from typing import Protocol

from anapp.application.domain.model.identifier.transaction_id import TransactionId
from anapp.application.domain.model.identifier.user_id import UserId
from anapp.application.domain.model.user_transaction import UserTransaction

class FindUserTransactionPort(Protocol):
    def find_user_transaction(
            self, 
            transaction_id: TransactionId, 
            user_id: UserId) -> UserTransaction:
        return NotImplementedError()

