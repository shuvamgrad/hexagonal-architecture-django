from typing import Protocol

from anapp.application.port.api.command.transaction_command import TransactionCommand
from anapp.application.domain.model.transaction_result import TransactionResult

class UserTransactionUseCase(Protocol):
    def make_transaction(self, command: TransactionCommand) -> TransactionResult:
        return NotImplementedError()