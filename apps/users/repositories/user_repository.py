from typing import Optional
import abc
from core.exceptions import NotFoundException, AlreadyExistException
from core.utils.converters.user_converter import UserRepositoryConverter
from apps.users.models import User
from apps.users.entities import UserEntity


class UserRepository:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    async def _user_is_exist(self, entity: UserEntity) -> bool:
        pass

    @abc.abstractmethod
    async def save_user(self, entity: UserEntity) -> UserEntity:
        pass

    @abc.abstractmethod
    async def update_user(self, user_id: int, query: dict) -> UserEntity:
        pass

    @abc.abstractmethod
    async def get_user(self, query: dict) -> UserEntity:
        pass

    @abc.abstractmethod
    async def get_user_by_id(self, user_id: int) -> UserEntity:
        pass

    @abc.abstractmethod
    async def get_user_list(self, offset: int, limit: int):
        pass

    @abc.abstractmethod
    async def user_login(self, email: str, password: str, join_type: str) -> Optional[UserEntity]:
        pass


class UserPGRepository(UserRepository):
    def __init__(self):
        self.converter = UserRepositoryConverter()

    async def _user_is_exist(self, entity: UserEntity) -> bool:
        user = await User.query.where(User.email == entity.email).gino.first()
        if user:
            return True
        return False

    async def save_user(self, entity: UserEntity) -> UserEntity:
        if self._user_is_exist(entity=entity):
            raise AlreadyExistException

        user_dict = self.converter.user_entity_to_dict(entity=entity)
        user = await User.create(**user_dict)
        return self.converter.user_model_to_entity(model=user)

    async def update_user(self, user_id: int, query: dict) -> UserEntity:
        user = await User.get(user_id)
        await user.update(**query).apply()
        return self.converter.user_model_to_entity(model=user)

    async def get_user(self, query: dict) -> UserEntity:
        user = await User.query.gino.first(**query)
        if user is None:
            raise NotFoundException
        return self.converter.user_model_to_entity(model=user)

    async def get_user_by_id(self, user_id: int) -> UserEntity:
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

    async def user_login(self, email: str, password: str, join_type: str) -> Optional[UserEntity]:
        user = await User.query.where(User.email == email)\
            .where(User.password == password)\
            .where(User.join_type == join_type)\
            .gino.first()

        if user is None:
            return None
        return self.converter.user_model_to_entity(model=user)
