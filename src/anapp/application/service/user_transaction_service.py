
from anapp.application.port.spi.find_user_transaction_port import FindUserTransactionPort
from anapp.application.port.spi.save_user_transaction_port import SaveUserTransactionPort
from anapp.application.port.api.command.transaction_command import TransactionCommand
from anapp.application.port.api.transaction_use_case import UserTransactionUseCase
from anapp.application.domain.model.transaction_result import TransactionResult
from anapp.application.domain.model.transaction_result import SuccessfulTransactionResult

class UserTransactionService(
    UserTransactionUseCase
):
    _find_user_transaction: FindUserTransactionPort
    _save_user_transaction: SaveUserTransactionPort

    def __init__(self, find_user_transaction: FindUserTransactionPort, save_user_transaction: SaveUserTransactionPort):
        self._find_user_transaction = find_user_transaction
        self._save_user_transaction = save_user_transaction

    def make_transaction(self, command: TransactionCommand) -> TransactionResult:
        transaction_user = self._find_user_transaction.find_user_transaction(
            user_id=command.user_id,
            transaction_id=command.transaction_id
        )

        transaction_result = transaction_user.make_transaction(command.transaction_id, command.amount)

        match transaction_result:
            case SuccessfulTransactionResult():
                self._save_user_transaction.save_transaction(transaction_user)
        return transaction_result