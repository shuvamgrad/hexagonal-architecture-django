from typing import cast, List

from anapp.application.adapter.spi.persistence.entity.transactions_entity import TransactionsEntity
from anapp.application.adapter.spi.persistence.entity.user_transaction_entity import UserTransactionEntity
from anapp.application.adapter.spi.persistence.exceptions.user_not_found import UserNotFound
from anapp.application.domain.model.identifier.transaction_id import TransactionId
from anapp.application.domain.model.identifier.user_id import UserId
from anapp.application.domain.model.user_transaction import UserTransaction, TransactionAmounts
from anapp.application.domain.model.balance import Balance
from anapp.application.domain.model.amount import Amount
from anapp.application.port.spi.find_user_transaction_port import FindUserTransactionPort
from anapp.application.port.spi.save_user_transaction_port import SaveUserTransactionPort

class UserTransactionRespository(
    FindUserTransactionPort,
    SaveUserTransactionPort
):
    
    def find_user_transaction(self, transaction_id: TransactionId, user_id: UserId) -> UserTransaction:
        user_entity = self._get_user_entity(user_id)
        transactions = self._get_all_transactions(user_id, transaction_id)
        return UserTransaction(
            user_id,
            Balance(user_entity.balance),
            transactions
        )

    
    def _get_user_entity(self, user_id: UserId) -> UserTransactionEntity:
        try:
            return UserTransactionEntity.objects.get(user_id=user_id)
        except UserTransactionEntity.DoesNotExist as e:
            raise UserNotFound from e
    
    def _get_all_transactions(self, user_id: UserId, transaction_id: TransactionId) -> List[TransactionAmounts]:
        transaction_entity = TransactionsEntity.objects.filter(
            user_id=user_id,
            transaction_id=transaction_id
        ).first()
        if transaction_entity is not None:
            transaction = self._get_transaction_entity_to_domain_model(transaction_entity)
            return [transaction]
        else:
            return []
        
    def save_transaction(self, user_transaction: UserTransaction) -> UserTransaction:
        saved_transaction_entity = self._save_transaction_entity(
            user_transaction.transactions
        )
        user_entity = self._get_user_entity(user_transaction.id)
        user_entity.balance-=user_transaction.transactions[0].amount
        user_entity.save()
        saved_transaction_model = [self._get_transaction_entity_to_domain_model(entity) for entity in saved_transaction_entity]
        return UserTransaction(
            id=user_transaction.id,
            balance=Balance(user_entity.balance),
            transactions=saved_transaction_model
        )

    
    def _save_transaction_entity(self, transactions: List[TransactionAmounts]):
        saved_transaction_entity: List[TransactionsEntity] = []
        for transact in transactions:
            transact_entity = self._get_domain_model_to_entity(transact)
            transact_entity.save()
            saved_transaction_entity.append(transact_entity)
        return saved_transaction_entity
    

    def _get_transaction_entity_to_domain_model(self, entity: TransactionsEntity) -> TransactionAmounts:
        return TransactionAmounts(
            TransactionId(entity.transaction_id),
            UserId(entity.user_id),
            Amount(entity.amount)
        )

    def _get_domain_model_to_entity(self, model: TransactionAmounts) -> TransactionsEntity:
        return TransactionsEntity(
            transaction_id=model.transaction_id,
            user_id=model.user_id,
            amount=model.amount 
        )
    

         