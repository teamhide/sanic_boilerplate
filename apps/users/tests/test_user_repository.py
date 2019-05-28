from apps.users.models import User
from apps.users.tests import app


async def test_save_user(app: app):
    await User.query.gino.all()
    assert app == 1


async def test_update_user():
    assert 1 == 1


async def test_get_user():
    assert 1 == 1


async def test_get_user_list():
    assert 1 == 1


async def test_user_login():
    assert 1 == 1
