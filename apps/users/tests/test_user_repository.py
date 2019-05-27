from apps.users.entities import UserEntity


class TestUserRepository:
    async def test_save_user(self, entity: UserEntity) -> UserEntity:
        assert 1 == 2

    async def test_update_user(self, user_id: int, query: dict) -> UserEntity:
        assert 1 == 2

    async def test_get_user(self, user_id: int) -> UserEntity:
        assert 1 == 2

    async def test_get_user_list(self, offset: int, limit: int):
        assert 1 == 2

    async def test_user_login(self, email: str, password: str, join_type: str) -> UserEntity:
        assert 1 == 2
