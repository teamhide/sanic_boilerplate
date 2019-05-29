import pytest
from core.tests import app
from apps.users.tests import create_user, user_data_1, login_interactor, create_user_interactor,\
    update_user_interactor, block_user_interactor, deactivate_user_interactor, update_user_to_admin_interactor,\
    get_user_interactor, get_user_list_interactor
from apps.users.dtos import LoginUserDto, CreateUserDto, UpdateUserDto, UpdateUserStateDto


async def test_login_interactor(app, login_interactor, create_user):
    # TODO: Hash 패스워드 삽입 후 비교 필요
    pass
    # dto = LoginUserDto(
    #     email=user_data_1['email'],
    #     password=user_data_1['password'],
    #     join_type=user_data_1['join_type']
    # )
    # result = await login_interactor.execute(dto=dto)
    # print(result)


async def test_create_user_interactor(app, create_user_interactor):
    dto = CreateUserDto(
        email=user_data_1['email'],
        password1=user_data_1['password'],
        password2=user_data_1['password'],
        nickname=user_data_1['nickname'],
        gender=user_data_1['gender'],
        join_type=user_data_1['join_type']
    )
    user = await create_user_interactor.execute(dto=dto)
    assert user.email == user_data_1['email']
    assert user.password != user_data_1['password']
    assert user.nickname == user_data_1['nickname']
    assert user.gender == user_data_1['gender']
    assert user.join_type == user_data_1['join_type']


async def test_update_user_interactor(app, create_user, update_user_interactor):
    # TODO: UpdateUserInteractor 구현 완료 후 추가 필요
    dto = UpdateUserDto(
        password='1',
        target_field='nickname',
        value='john'
    )


async def test_block_user_interactor(app, create_user, block_user_interactor):
    dto = UpdateUserStateDto(
        token=1,
        user_id=2
    )


async def test_deactivate_user_interactor(app):
    pass


async def test_update_user_to_admin_interactor(app):
    pass


async def test_get_user_interactor(app):
    pass


async def test_get_user_list_interactor(app):
    pass
