import requests
import bcrypt
from typing import Union, NoReturn, Optional, List
from core.utils.converters.user_converter import UserInteractorConverter
from core.exceptions import PermissionErrorException, LoginFailException, InvalidJoinTypeException, \
    SocialLoginFailException
from core.utils import TokenHelper, QueryBuilder
from apps.users.repositories import UserPGRepository
from apps.users.dtos import RegisterUserDto, UpdateUserDto, LoginDto, UserListDto, UpdateUserStateDto
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
    async def execute(self, dto: LoginDto) -> Union[str, NoReturn]:
        """
        유저 로그인 함수

        :param dto: CreateUserDto
        :return: token|NoReturn
        """

        hashed_password = await self._create_hash(password=dto.password)
        user = await self.repository.user_login(email=dto.email, password=hashed_password, join_type=dto.join_type)
        if user is None:
            raise LoginFailException

        if not await self._check_password(password=dto.password, stored_hash=user.password):
            raise PermissionErrorException

        return self.token.encode(user_id=user.id)

    async def _check_password(self, password: str, stored_hash: str) -> bool:
        return await bcrypt.hashpw(password.encode('utf8'), stored_hash.encode('utf8')) == stored_hash.encode('utf8')


class RegisterUserInteractor(UserInteractor):
    def __init__(self):
        super().__init__()
        self.kakao_url = 'https://kauth.kakao.com/oauth/token'
        self.facebook_url = 'http://facebook.com'
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

    async def execute(self, dto: RegisterUserDto) -> Union[UserEntity, NoReturn]:
        """
        유저 회원가입 함수

        :param dto: CreateUserDto
        :return: UserEntity|NoReturn
        """

        if dto.password1 != dto.password2:
            raise PermissionErrorException

        if dto.join_type == 'kakao':
            await self._register_by_kakao(dto=dto)
        elif dto.join_type == 'facebook':
            await self._register_by_facebook(dto=dto)
        elif dto.join_type == 'default':
            await self._register_by_default(dto=dto)
        else:
            raise InvalidJoinTypeException

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

    async def _register_by_kakao(self, dto: RegisterUserDto) -> bool:
        # TODO: 소셜 로그인 연동 필요
        data = {'email': dto.email, 'password': dto.password1}
        req = requests.post(url=self.kakao_url, data=data, headers=self.headers)

        if req.status_code != 200:
            raise SocialLoginFailException

        access_token = req.text.encode('utf8')
        if not access_token:
            raise SocialLoginFailException
        return True

    async def _register_by_facebook(self, dto: RegisterUserDto) -> bool:
        # TODO: 소셜 로그인 연동 필요
        data = {'email': dto.email, 'password': dto.password1}
        req = requests.post(url=self.facebook_url, data=data, headers=self.headers)

        if req.status_code != 200:
            raise SocialLoginFailException

        access_token = req.text.encode('utf8')
        if not access_token:
            raise SocialLoginFailException
        return True

    async def _register_by_default(self, dto: RegisterUserDto):
        pass


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
            raise PermissionErrorException

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
            raise PermissionErrorException

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
            raise PermissionErrorException

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
            raise PermissionErrorException

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
