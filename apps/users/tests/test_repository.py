from apps.users.entities import UserEntity


class TestUserRepository:
    async def test_save_user(self, entity: UserEntity) -> UserEntity:
        pass

    async def test_update_user(self, user_id: int, query: dict) -> UserEntity:
        pass

    async def test_get_user(self, user_id: int) -> UserEntity:
        pass

    async def test_get_user_list(self, offset: int, limit: int):
        pass

    async def test_user_login(self, email: str, password: str, join_type: str) -> UserEntity:
        pass
