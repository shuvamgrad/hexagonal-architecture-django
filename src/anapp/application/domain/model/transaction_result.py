from __future__ import annotations
from dataclasses import dataclass
from anapp.application.domain.model.identifier.user_id import UserId
from anapp.application.domain.model.identifier.transaction_id import TransactionId
from anapp.application.domain.model.amount import Amount


class TransactionResult:
    def to_message(self) -> str:
        return NotImplementedError()

@dataclass
class ConflictAmountResult(TransactionResult):
    def to_message(self) -> str:
        return f"Amount cannot be less than ZERO!"

@dataclass
class InsufficientBalanceResult(TransactionResult):
    user_id: UserId

    def to_message(self) -> str:
        return f"User {self.user_id} does not have enough balance!"

@dataclass
class SuccessfulTransactionResult(TransactionResult):
    user_id: UserId
    transaction_id: TransactionId
    amount: Amount
