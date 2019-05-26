import jwt
from typing import Union, NoReturn
from core.converters.user_converter import UserInteractorConverter
from core.exceptions import DoNotHavePermissionException, LoginFailException
from core.config import JWT_SECRET_KEY, JWT_ALGORITHM
from apps.users.repositories import UserPostgreSQLRepository
from apps.users.dtos import CreateUserDto, UpdateUserDto, LoginUserDto
from apps.users.entities import UserEntity


class UserInteractor:
    def __init__(self):
        self.repository = UserPostgreSQLRepository()
        self.converter = UserInteractorConverter()


class LoginInteractor(UserInteractor):
    async def execute(self, dto: LoginUserDto) -> Union[str, NoReturn]:
        """
        유저 로그인 함수

        :param dto: CreateUserDto
        :return: token
        """
        user = self.repository.user_login(email=dto.email, password=dto.password, join_type=dto.join_type)
        if user is False:
            raise LoginFailException
        return self._make_jwt(entity=user)

    async def _make_jwt(self, entity: UserEntity) -> str:
        return jwt.encode(
            payload={'email': entity.email},
            key=JWT_SECRET_KEY,
            algorithm=JWT_ALGORITHM
        )


class CreateUserInteractor(UserInteractor):
    async def execute(self, dto: CreateUserDto) -> Union[UserEntity, NoReturn]:
        """
        유저를 생성하는 함수

        :param dto: CreateUserDto
        :return: UserEntity
        """

        if dto.password1 != dto.password2:
            raise DoNotHavePermissionException

        user_entity = UserEntity(
            email=dto.email,
            password=dto.password1,
            nickname=dto.nickname,
            gender=dto.gender,
            join_type=dto.join_type,
        )

        await self.repository.save_user(entity=user_entity)
        return user_entity


class UpdateUserInteractor(UserInteractor):
    def execute(self, dto: UpdateUserDto):
        pass


class BlockUserInteractor(UserInteractor):
    def execute(self, dto):
        pass


class DeactivateUserInteractor(UserInteractor):
    def execute(self, dto):
        pass


class UpdateUserToAdminInteractor(UserInteractor):
    def execute(self, dto):
        pass


class GetUserInteractor(UserInteractor):
    async def execute(self, user_id: int):
        user = await self.repository.get_user(user_id=user_id)
        print(user)


class GetUserListInteractor(UserInteractor):
    def execute(self, dto):
        pass
