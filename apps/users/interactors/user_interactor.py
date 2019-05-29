import bcrypt
from typing import Union, NoReturn, Optional, List
from core.utils.converters.user_converter import UserInteractorConverter
from core.exceptions import DoNotHavePermissionException, LoginFailException
from core.utils import TokenHelper, QueryBuilder
from apps.users.repositories import UserPGRepository
from apps.users.dtos import CreateUserDto, UpdateUserDto, LoginUserDto, UserListDto, UpdateUserStateDto
from apps.users.entities import UserEntity


class UserInteractor:
    def __init__(self):
        self.repository = UserPGRepository()
        self.converter = UserInteractorConverter()
        self.token = TokenHelper()
        self.builder = QueryBuilder()

    async def _create_hash(self, password: str) -> str:
        salt = bcrypt.gensalt()
        return str(bcrypt.hashpw(password=password.encode('utf8'), salt=salt))


class LoginInteractor(UserInteractor):
    async def execute(self, dto: LoginUserDto) -> Union[str, NoReturn]:
        """
        유저 로그인 함수

        :param dto: CreateUserDto
        :return: token|NoReturn
        """
        user = await self.repository.user_login(email=dto.email, password=dto.password, join_type=dto.join_type)
        if user is None:
            raise LoginFailException

        if not await self._check_password(password=dto.password, stored_hash=user.password):
            raise DoNotHavePermissionException

        return self.token.encode(user_id=user.id)

    async def _check_password(self, password: str, stored_hash: str) -> bool:
        return await bcrypt.hashpw(password.encode('utf8'), stored_hash.encode('utf8')) == stored_hash


class CreateUserInteractor(UserInteractor):
    async def execute(self, dto: CreateUserDto) -> Union[UserEntity, NoReturn]:
        """
        유저를 생성하는 함수

        :param dto: CreateUserDto
        :return: UserEntity|NoReturn
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


class UpdateUserInteractor(UserInteractor):
    async def execute(self, user_id: int, dto: UpdateUserDto) -> Union[UserEntity, NoReturn]:
        """
        유저를 수정하는 함수

        :param user_id: int
        :param dto: UpdateUserDto
        :return: UserEntity|NoReturn
        """

        self.builder.user_id = user_id
        self.builder.password = self._create_hash(password=dto.password)
        user = await self.repository.get_user(query=self.builder.query())
        if user is None:
            raise DoNotHavePermissionException

        query = {dto.target_field: dto.value}
        return self.repository.update_user(user_id=user_id, query=query)


class BlockUserInteractor(UserInteractor):
    async def execute(self, dto: UpdateUserStateDto) -> Optional[NoReturn]:
        """
        유저를 블락처리 시키는 함수

        :param dto: UpdateUserStateDto
        :return: NoReturn|None
        """

        payload = self.token.decode(token=dto.token)

        is_admin = await self.repository.get_user_by_id(user_id=payload.get('user_id'))
        if is_admin is False:
            raise DoNotHavePermissionException

        self.builder.is_block = True
        await self.repository.update_user(user_id=dto.user_id, query=self.builder.query())


class DeactivateUserInteractor(UserInteractor):
    async def execute(self, dto: UpdateUserStateDto) -> Optional[NoReturn]:
        """
        유저를 휴면처리 시키는 함수

        :param dto: UpdateUserStateDto
        :return: NoReturn|None
        """

        payload = self.token.decode(token=dto.token)

        is_admin = self.repository.get_user_by_id(user_id=payload.get('user_id'))
        if is_admin is False:
            raise DoNotHavePermissionException

        self.builder.is_active = False
        await self.repository.update_user(user_id=dto.user_id, query=self.builder.query())


class UpdateUserToAdminInteractor(UserInteractor):
    async def execute(self, dto: UpdateUserStateDto) -> Optional[NoReturn]:
        """
        유저를 관리자로 변경처리 시키는 함수

        :param dto: UpdateUserStateDto
        :return: NoReturn|None
        """

        payload = self.token.decode(token=dto.token)

        is_admin = self.repository.get_user_by_id(user_id=payload.get('user_id'))
        if is_admin is False:
            raise DoNotHavePermissionException

        self.builder.is_admin = True
        await self.repository.update_user(user_id=dto.user_id, query=self.builder.query())


class GetUserInteractor(UserInteractor):
    async def execute(self, user_id: int) -> Union[UserEntity, NoReturn]:
        """
        단일 유저를 가져오는 함수

        :param user_id: int
        :return: UserEntity|NoReturn
        """

        return await self.repository.get_user_by_id(user_id=user_id)


class GetUserListInteractor(UserInteractor):
    async def execute(self, dto: UserListDto = None) -> Union[List[UserEntity], NoReturn]:
        """
        유저 리스트를 가져오는 함수

        :param dto: UserListDto
        :return: List[UserEntity]|NoReturn
        """
        return await self.repository.get_user_list(offset=dto.offset, limit=dto.limit)
