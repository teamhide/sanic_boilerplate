from apps.users.models import User
from apps.users.tests import app


class TestUserRepository:
    async def test_save_user(self, app: app):
        await User.query.gino.all()
        assert app == 1

    async def test_update_user(self):
        assert 1 == 1

    async def test_get_user(self):
        assert 1 == 1

    async def test_get_user_list(self):
        assert 1 == 1

    async def test_user_login(self):
        assert 1 == 1
