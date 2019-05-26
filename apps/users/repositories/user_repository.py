import abc
from core.converters.user_converter import UserRepositoryConverter
from apps.users.models import User
from apps.users.entities import UserEntity


class UserRepository:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def save_user(self, entity: UserEntity) -> UserEntity:
        pass

    @abc.abstractmethod
    def update_user(self, query: dict) -> UserEntity:
        pass

    @abc.abstractmethod
    def delete_user(self) -> bool:
        pass

    @abc.abstractmethod
    def get_user(self, user_id: int) -> UserEntity:
        pass

    @abc.abstractmethod
    def get_user_list(self, offset: int, limit: int):
        pass

    @abc.abstractmethod
    def user_login(self, email: str, password: str, join_type: str) -> UserEntity:
        pass


class UserPostgreSQLRepository(UserRepository):
    def __init__(self):
        self.converter = UserRepositoryConverter()

    def save_user(self, entity: UserEntity) -> UserEntity:
        user = User.create(entity.__dict__)
        return user

    def update_user(self, query: dict) -> UserEntity:
        pass

    def delete_user(self) -> bool:
        pass

    def get_user(self, user_id: int) -> UserEntity:
        pass

    def get_user_list(self, offset: int, limit: int):
        pass

    def user_login(self, email: str, password: str, join_type: str) -> UserEntity:
        user = User.get(email=email, password=password, join_type=join_type)
        return self.converter.user_model_to_entity(model=user)
