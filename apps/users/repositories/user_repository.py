import abc
from core.converters.user_converter import UserRepositoryConverter
from core.exceptions import NotFoundException
from apps.users.models import User
from apps.users.entities import UserEntity


class UserRepository:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    async def save_user(self, entity: UserEntity) -> UserEntity:
        pass

    @abc.abstractmethod
    async def update_user(self, user_id: int, query: dict) -> UserEntity:
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


class UserPGRepository(UserRepository):
    def __init__(self):
        self.converter = UserRepositoryConverter()

    async def save_user(self, entity: UserEntity) -> UserEntity:
        user = self.converter.user_entity_to_dict(entity=entity)
        user.pop('id')
        user = await User.create(**user)
        return self.converter.user_model_to_entity(model=user)

    async def update_user(self, user_id: int, query: dict) -> UserEntity:
        user = await User.get(user_id)
        await user.update(**query).apply()
        return self.converter.user_model_to_entity(model=user)

    async def get_user(self, user_id: int) -> UserEntity:
        user = await User.get(user_id)
        if user is None:
            raise NotFoundException
        return self.converter.user_model_to_entity(model=user)

    async def get_user_list(self, offset: int = 1, limit: int = 1):
        users = await User.query.gino.all()
        if users is None:
            raise NotFoundException
        user_entity = [
            self.converter.user_model_to_entity(model=user)
            for user in users
        ]
        return user_entity

    async def user_login(self, email: str, password: str, join_type: str) -> UserEntity:
        user = await User.get(email=email, password=password, join_type=join_type)
        return self.converter.user_model_to_entity(model=user)
