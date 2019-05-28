import pytest
from apps.users.tests import app
from apps.users.models import User


# @pytest.fixture
# async def app():
#     await db.set_bind('postgresql://localhost/sanic')


async def test_save_user(app):
    u1 = await User.create(nickname='fantix')


async def test_update_user():
    assert 1 == 1


async def test_get_user():
    assert 1 == 1


async def test_get_user_list():
    assert 1 == 1


async def test_user_login():
    assert 1 == 1
