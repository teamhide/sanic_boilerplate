import abc
from core.converters.user_converter import UserRepositoryConverter
from apps.users.models import User
from apps.users.entities import UserEntity


class UserRepository:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    async def save_user(self, entity: UserEntity) -> UserEntity:
        pass

    @abc.abstractmethod
    async def update_user(self, query: dict) -> UserEntity:
        pass

    @abc.abstractmethod
    async def delete_user(self) -> bool:
        pass

    @abc.abstractmethod
    async def get_user(self, user_id: int) -> UserEntity:
        pass

    @abc.abstractmethod
    async def get_user_list(self, offset: int, limit: int):
        pass

    @abc.abstractmethod
    async def user_login(self, email: str, password: str, join_type: str) -> UserEntity:
        pass


class UserPostgreSQLRepository(UserRepository):
    def __init__(self):
        self.converter = UserRepositoryConverter()

    async def save_user(self, entity: UserEntity) -> UserEntity:
        user = await User.create(**self.converter.user_entity_to_dict(entity=entity))
        return self.converter.user_model_to_entity(model=user)

    async def update_user(self, query: dict) -> UserEntity:
        pass

    async def delete_user(self) -> bool:
        pass

    async def get_user(self, user_id: int) -> UserEntity:
        return await User.get(user_id)

    async def get_user_list(self, offset: int, limit: int):
        pass

    async def user_login(self, email: str, password: str, join_type: str) -> UserEntity:
        user = await User.get(email=email, password=password, join_type=join_type)
        return self.converter.user_model_to_entity(model=user)
