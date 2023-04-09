from typing import Protocol

from anapp.application.domain.model.user_transaction import UserTransaction

class SaveUserTransactionPort(Protocol):
    def save_transaction(self, user_transaction: UserTransaction) -> UserTransaction:
        return NotImplementedError()