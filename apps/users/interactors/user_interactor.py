import jwt
from typing import Union, NoReturn, Optional
from core.converters.user_converter import UserInteractorConverter
from core.exceptions import DoNotHavePermissionException, LoginFailException
from core.config import JWT_SECRET_KEY, JWT_ALGORITHM
from core.utils import TokenHelper
from apps.users.repositories import UserPGRepository
from apps.users.dtos import CreateUserDto, UpdateUserDto, LoginUserDto, UserListDto, UpdateUserStateDto
from apps.users.entities import UserEntity


class UserInteractor:
    def __init__(self):
        self.repository = UserPGRepository()
        self.converter = UserInteractorConverter()


class LoginInteractor(UserInteractor):
    async def execute(self, dto: LoginUserDto) -> Union[str, NoReturn]:
        """
        유저 로그인 함수

        :param dto: CreateUserDto
        :return: token
        """
        user = await self.repository.user_login(email=dto.email, password=dto.password, join_type=dto.join_type)
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
    async def execute(self, dto: UpdateUserStateDto) -> Optional[NoReturn]:
        payload = TokenHelper().decode(token=dto.token)

        # TODO: 토큰의 권한이 관리자인지 확인하는 루틴 추가 필요

        # Build Query
        query = {'is_block': True}

        await self.repository.update_user(user_id=dto.user_id, query=query)


class DeactivateUserInteractor(UserInteractor):
    async def execute(self, dto: UpdateUserStateDto):
        payload = TokenHelper().decode(token=dto.token)

        # TODO: 토큰의 권한이 관리자인지 확인하는 루틴 추가 필요

        # Build Query
        query = {'is_active': False}

        await self.repository.update_user(user_id=dto.user_id, query=query)


class UpdateUserToAdminInteractor(UserInteractor):
    async def execute(self, dto: UpdateUserStateDto):
        payload = TokenHelper().decode(token=dto.token)

        # TODO: 토큰의 권한이 관리자인지 확인하는 루틴 추가 필요

        # Build Query
        query = {'is_admin': True}

        await self.repository.update_user(user_id=dto.user_id, query=query)


class GetUserInteractor(UserInteractor):
    async def execute(self, user_id: int):
        return await self.repository.get_user(user_id=user_id)


class GetUserListInteractor(UserInteractor):
    async def execute(self, dto: UserListDto = None):
        return await self.repository.get_user_list(**dto.__dict__)
