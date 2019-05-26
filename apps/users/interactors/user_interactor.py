import bcrypt
from typing import Union, NoReturn, Optional
from core.converters.user_converter import UserInteractorConverter
from core.exceptions import DoNotHavePermissionException, LoginFailException
from core.utils import TokenHelper
from apps.users.repositories import UserPGRepository
from apps.users.dtos import CreateUserDto, UpdateUserDto, LoginUserDto, UserListDto, UpdateUserStateDto
from apps.users.entities import UserEntity


class UserInteractor:
    def __init__(self):
        self.repository = UserPGRepository()
        self.converter = UserInteractorConverter()
        self.token = TokenHelper()


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

        if not await self._check_password(password=dto.password, stored_hash=user.password):
            raise DoNotHavePermissionException

        return self.token.encode(user_id=user.id)

    async def _check_password(self, password: str, stored_hash: str) -> bool:
        return await bcrypt.hashpw(password.encode('utf8'), stored_hash) == stored_hash


class CreateUserInteractor(UserInteractor):
    async def execute(self, dto: CreateUserDto) -> Union[UserEntity, NoReturn]:
        """
        유저를 생성하는 함수

        :param dto: CreateUserDto
        :return: UserEntity
        """

        if dto.password1 != dto.password2:
            raise DoNotHavePermissionException

        hashed_password = await self._create_hash(password=dto.password1)

        user_entity = UserEntity(
            email=dto.email,
            password=hashed_password,
            nickname=dto.nickname,
            gender=dto.gender,
            join_type=dto.join_type,
        )

        await self.repository.save_user(entity=user_entity)
        return user_entity

    async def _create_hash(self, password: str) -> str:
        salt = bcrypt.gensalt()
        return await bcrypt.hashpw(password=password, salt=salt)


class UpdateUserInteractor(UserInteractor):
    def execute(self, dto: UpdateUserDto):
        pass


class BlockUserInteractor(UserInteractor):
    async def execute(self, dto: UpdateUserStateDto) -> Optional[NoReturn]:
        """
        유저를 블락처리 시키는 함수

        :param dto: UpdateUserStateDto
        :return: None
        """

        payload = self.token.decode(token=dto.token)

        is_admin = self.repository.get_user(user_id=payload.get('user_id'))
        if is_admin is False:
            raise DoNotHavePermissionException

        query = {'is_block': True}

        await self.repository.update_user(user_id=dto.user_id, query=query)


class DeactivateUserInteractor(UserInteractor):
    async def execute(self, dto: UpdateUserStateDto):
        """
        유저를 휴면처리 시키는 함수

        :param dto: UpdateUserStateDto
        :return: None
        """

        payload = self.token.decode(token=dto.token)

        is_admin = self.repository.get_user(user_id=payload.get('user_id'))
        if is_admin is False:
            raise DoNotHavePermissionException

        query = {'is_active': False}

        await self.repository.update_user(user_id=dto.user_id, query=query)


class UpdateUserToAdminInteractor(UserInteractor):
    async def execute(self, dto: UpdateUserStateDto):
        """
        유저를 관리자로 변경처리 시키는 함수

        :param dto: UpdateUserStateDto
        :return: None
        """

        payload = self.token.decode(token=dto.token)

        is_admin = self.repository.get_user(user_id=payload.get('user_id'))
        if is_admin is False:
            raise DoNotHavePermissionException

        query = {'is_admin': True}

        await self.repository.update_user(user_id=dto.user_id, query=query)


class GetUserInteractor(UserInteractor):
    async def execute(self, user_id: int):
        return await self.repository.get_user(user_id=user_id)


class GetUserListInteractor(UserInteractor):
    async def execute(self, dto: UserListDto = None):
        return await self.repository.get_user_list(**dto.__dict__)
