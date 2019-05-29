import pytest
from apps.users.repositories import UserPGRepository
from apps.users.interactors import LoginInteractor, CreateUserInteractor, UpdateUserInteractor, BlockUserInteractor,\
    DeactivateUserInteractor, UpdateUserToAdminInteractor, GetUserInteractor, GetUserListInteractor
from apps.users.models import User
from apps.users.entities import UserEntity


user_data_1 = {
    'email': 'sharehead@gmail.com',
    'password': '123',
    'nickname': 'hide',
    'gender': 'M',
    'join_type': 'default',
    'is_active': False,
    'is_block': False,
    'is_admin': False
}
user_data_2 = {
    'email': 'test@gmail.com',
    'password': '123',
    'nickname': 'test',
    'gender': 'F',
    'join_type': 'facebook',
    'is_active': True,
    'is_block': False,
    'is_admin': True
}


@pytest.fixture
def repository():
    return UserPGRepository()


@pytest.fixture
def login_interactor():
    return LoginInteractor()


@pytest.fixture
def create_user_interactor():
    return CreateUserInteractor()


@pytest.fixture
def update_user_interactor():
    return UpdateUserInteractor()


@pytest.fixture
def block_user_interactor():
    return BlockUserInteractor()


@pytest.fixture
def deactivate_user_interactor():
    return DeactivateUserInteractor()


@pytest.fixture
def update_user_to_admin_interactor():
    return UpdateUserToAdminInteractor()


@pytest.fixture
def get_user_interactor():
    return GetUserInteractor()


@pytest.fixture
def get_user_list_interactor():
    return GetUserListInteractor()


@pytest.fixture
async def create_user():
    await User.create(**user_data_1)


@pytest.fixture
def user_entity():
    return UserEntity(
        email=user_data_1['email'],
        password=user_data_1['password'],
        nickname=user_data_1['nickname'],
        gender=user_data_1['gender'],
        join_type=user_data_1['join_type'],
        is_active=user_data_1['is_active'],
        is_block=user_data_1['is_block'],
        is_admin=user_data_1['is_admin'],
    )


@pytest.fixture
async def create_user_list():
    await User.create(**user_data_1)
    await User.create(**user_data_2)
