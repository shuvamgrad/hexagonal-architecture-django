from typing import Dict, Any


from anapp.application.adapter.spi.persistence.repository.user_transaction_repository import UserTransactionRespository
from anapp.application.service.user_transaction_service import UserTransactionService
from anapp.application.adapter.api.http.transaction_view import TransactionView

def build_production_dependencies_container() -> Dict[str, Any]:
    user_transaction_respository = UserTransactionRespository()
    user_transaction_service = UserTransactionService(
        find_user_transaction=user_transaction_respository,
        save_user_transaction=user_transaction_respository
    )
    transaction_view = TransactionView.as_view(
        transaction_use_case = user_transaction_service
    )
    return {'transaction_view': transaction_view}

