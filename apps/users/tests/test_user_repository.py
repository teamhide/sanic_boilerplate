import pytest
from core.tests import app
from apps.users.models import User
from apps.users.entities import UserEntity
from apps.users.dtos import UserListDto, LoginUserDto
from apps.users.repositories import UserPGRepository


@pytest.fixture
def user_entity():
    return UserEntity(
        email='sharehead@gmail.com',
        password='12345',
        nickname='hide',
        gender='M',
        join_type='default',
        is_active=False,
        is_block=False,
        is_admin=False,
    )


@pytest.fixture
def repository():
    return UserPGRepository()


@pytest.fixture
async def create_user():
    return await User.create(

    )

@pytest.fixture
def dto():
    return


async def test_save_user(app, user_entity: UserEntity, repository: UserPGRepository):
    user = await repository.save_user(entity=user_entity)
    assert isinstance(user, UserEntity) is True
    assert user.email == user_entity.email
    assert user.password == user_entity.password
    assert user.nickname == user_entity.nickname
    assert user.gender == user_entity.gender
    assert user.join_type == user_entity.join_type
    assert user.is_active == user_entity.is_active
    assert user.is_block == user_entity.is_block
    assert user.is_admin == user_entity.is_admin


async def test_update_user(app, user_entity: UserEntity, repository: UserPGRepository):
    assert 1 == 1


async def test_get_user(app, repository: UserPGRepository):
    assert 1 == 1


async def test_get_user_list(app, dto: UserListDto, repository: UserPGRepository):
    assert 1 == 1


async def test_user_login(app, dto: LoginUserDto, repository: UserPGRepository):
    assert 1 == 1
