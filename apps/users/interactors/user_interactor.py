from apps.users.repositories import UserPostgreSQLRepository


class UserInteractor:
    def __init__(self):
        self.repository = UserPostgreSQLRepository()


class CreateUserInteractor(UserInteractor):
    def execute(self, dto):
        pass


class UpdateUserInteractor(UserInteractor):
    def execute(self, dto):
        pass


class DeleteUserInteractor(UserInteractor):
    def execute(self, dto):
        pass


class BlockUserInteractor(UserInteractor):
    def execute(self, dto):
        pass


class GetUserInteractor(UserInteractor):
    def execute(self, dto):
        pass


class GetUserListInteractor(UserInteractor):
    def execute(self, dto):
        pass
