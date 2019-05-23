from core.converters.user_converter import UserInteractorConverter
from apps.users.repositories import UserPostgreSQLRepository
from apps.users.dtos import CreateUserDto, UpdateUserDto
from apps.users.entities import UserEntity


class UserInteractor:
    def __init__(self):
        self.repository = UserPostgreSQLRepository()
        self.converter = UserInteractorConverter()


class CreateUserInteractor(UserInteractor):
    def execute(self, dto: CreateUserDto):
        """권한 검사"""
        if dto.password1 != dto.password2:
            return

        """DTO -> Entity 변환"""
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

        """User 저장"""
        self.repository.save_user(entity=user_entity)


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
