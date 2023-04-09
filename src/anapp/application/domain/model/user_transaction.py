from __future__ import annotations
from dataclasses import dataclass, field

from anapp.application.domain.model.amount import Amount
from anapp.application.domain.model.balance import Balance
from anapp.application.domain.model.identifier.transaction_id import TransactionId
from anapp.application.domain.model.identifier.user_id import UserId 
from anapp.application.domain.model.transaction_result import (
    TransactionResult,
    SuccessfulTransactionResult,
    InsufficientBalanceResult,
    ConflictAmountResult
)

@dataclass
class UserTransaction:
    id: UserId
    balance: Balance
    transactions: list[TransactionAmounts] = field(default_factory=list)

    def make_transaction(
            self, 
            transaction_id: TransactionId,
            amount: Amount) -> TransactionResult:

        if amount <= 0:
            return ConflictAmountResult()
        
        if self._balance_not_enough_for_transaction(amount):
            return InsufficientBalanceResult(user_id=self.id)
        
        self.balance -= amount
        self.transactions.append(
            TransactionAmounts(transaction_id, self.id, amount)
        )
        return SuccessfulTransactionResult(self.id, transaction_id, amount)
    
    def _balance_not_enough_for_transaction(self, amount):
        return self.balance < amount
    
@dataclass
class TransactionAmounts:
    transaction_id: TransactionId
    user_id: UserId
    amount: Amount

