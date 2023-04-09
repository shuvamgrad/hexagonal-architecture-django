from http import HTTPStatus

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from anapp.application.port.api.transaction_use_case import UserTransactionUseCase
from anapp.application.port.api.command.transaction_command import TransactionCommand
from anapp.application.adapter.api.http.serializer.make_transaction_command_deserializer import MakeTransactionCommandDeserializer
from anapp.application.adapter.api.http.serializer.successfully_transaction_serializer import SuccessfullyTransactionSerializer
from anapp.application.adapter.api.http.problem_response import problem_response
from anapp.application.domain.model.transaction_result import TransactionResult
from anapp.application.domain.model.transaction_result import SuccessfulTransactionResult
from anapp.application.domain.model.transaction_result import InsufficientBalanceResult
from anapp.application.domain.model.transaction_result import ConflictAmountResult 
from anapp.application.util.assert_never import assert_never

class TransactionView(APIView):
    transaction_use_case: UserTransactionUseCase = None

    def __init__(self, transaction_use_case: UserTransactionUseCase):
        self.transaction_use_case = transaction_use_case
        super().__init__()

    def post(self, request: Request) -> Response:
        transaction_command = self._read_transaction_request(request)
        result = self.transaction_use_case.make_transaction(transaction_command)
        return self._build_response(result)
    

    def _read_transaction_request(self, request: Request) -> TransactionCommand:
        serializer = MakeTransactionCommandDeserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return serializer.create()
    
    def _build_response(self, transaction_result: TransactionResult) -> Response:
        response = None
        match transaction_result:
            case SuccessfulTransactionResult():
                response_data = SuccessfullyTransactionSerializer(transaction_result).data
                response = Response(response, status=HTTPStatus.CREATED)
            case InsufficientBalanceResult():
                response = problem_response(
                    title="Cannot make transaction",
                    detail=transaction_result.to_message(),
                    status=HTTPStatus.CONFLICT
                )
            case ConflictAmountResult():
                response = problem_response(
                    title="Cannot make transaction",
                    detail=transaction_result.to_message(),
                    status=HTTPStatus.BAD_REQUEST
                )
            case _:
                assert_never(transaction_result)
        return response