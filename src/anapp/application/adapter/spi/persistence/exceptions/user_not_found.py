from anapp.application.domain.model.identifier.user_id import UserId

class UserNotFound(RuntimeError):
    def __init__(self, user_id: UserId):
        super().__init__(f"User '{user_id}' not found")