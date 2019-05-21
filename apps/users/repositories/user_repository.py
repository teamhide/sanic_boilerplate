import abc
from apps.users.models import User


class UserRepository:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def save_user(self, query: dict):
        pass

    @abc.abstractmethod
    def update_user(self, query: dict):
        pass

    @abc.abstractmethod
    def delete_user(self):
        pass

    @abc.abstractmethod
    def get_user(self, user_id: int):
        pass

    @abc.abstractmethod
    def get_user_list(self, offset: int, limit: int):
        pass


class UserPostgreSQLRepository(UserRepository):
    def save_user(self, query: dict):
        pass

    def update_user(self, query: dict):
        pass

    def delete_user(self):
        pass

    def get_user(self, user_id: int):
        pass

    def get_user_list(self, offset: int, limit: int):
        pass
