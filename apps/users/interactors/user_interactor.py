from typing import Union, NoReturn
from core.converters.user_converter import UserInteractorConverter
from core.exceptions import DoNotHavePermissionException
from apps.users.repositories import UserPostgreSQLRepository
from apps.users.dtos import CreateUserDto, UpdateUserDto
from apps.users.entities import UserEntity


class UserInteractor:
    def __init__(self):
        self.repository = UserPostgreSQLRepository()
        self.converter = UserInteractorConverter()


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
            is_active=True,
            is_block=False,
            is_admin=False,
        )

        self.repository.save_user(entity=user_entity)
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
    def execute(self, user_id: int):
        pass


class GetUserListInteractor(UserInteractor):
    def execute(self, dto):
        pass
