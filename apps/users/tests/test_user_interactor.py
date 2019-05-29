import pytest
from core.tests import app
from apps.users.tests import login_interactor, create_user, user_data_1
from apps.users.dtos import LoginUserDto


async def test_login_interactor(app, login_interactor, create_user):
    pass
    # dto = LoginUserDto(
    #     email=user_data_1['email'],
    #     password=user_data_1['password'],
    #     join_type=user_data_1['join_type']
    # )
    # result = await login_interactor.execute(dto=dto)
    # print(result)


async def test_create_user_interactor(app):
    pass


async def test_update_user_interactor(app):
    pass


async def test_block_user_interactor(app):
    pass


async def test_deactivate_user_interactor(app):
    pass


async def test_update_user_to_admin_interactor(app):
    pass


async def test_get_user_interactor(app):
    pass


async def test_get_user_list_interactor(app):
    pass
