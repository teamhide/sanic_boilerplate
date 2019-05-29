import pytest
from core.tests import app
from apps.users.models import User
from apps.users.entities import UserEntity
from apps.users.repositories import UserPGRepository
from apps.users.tests import repository, user_data_1, user_data_2, create_user, user_entity, create_user_list


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


async def test_update_user(app, create_user, repository: UserPGRepository):
    updated_nickname = 'testhide'
    user = await repository.update_user(user_id=1, query={'nickname': updated_nickname})
    assert user.nickname == updated_nickname


async def test_get_user(app, create_user, user_entity: UserEntity, repository: UserPGRepository):
    user = await repository.get_user_by_id(user_id=1)
    assert isinstance(user, UserEntity) is True
    assert user.email == user_entity.email
    assert user.password == user_entity.password
    assert user.nickname == user_entity.nickname
    assert user.gender == user_entity.gender
    assert user.join_type == user_entity.join_type
    assert user.is_active == user_entity.is_active
    assert user.is_block == user_entity.is_block
    assert user.is_admin == user_entity.is_admin


async def test_get_user_list(app, create_user_list, repository: UserPGRepository):
    users = await repository.get_user_list()
    assert type(users) == list
    assert len(users) == 2

    assert isinstance(users[0], UserEntity) is True
    assert users[0].email == user_data_1['email']
    assert users[0].password == user_data_1['password']
    assert users[0].nickname == user_data_1['nickname']
    assert users[0].gender == user_data_1['gender']
    assert users[0].join_type == user_data_1['join_type']
    assert users[0].is_active == user_data_1['is_active']
    assert users[0].is_block == user_data_1['is_block']
    assert users[0].is_admin == user_data_1['is_admin']

    assert isinstance(users[1], UserEntity) is True
    assert users[1].email == user_data_2['email']
    assert users[1].password == user_data_2['password']
    assert users[1].nickname == user_data_2['nickname']
    assert users[1].gender == user_data_2['gender']
    assert users[1].join_type == user_data_2['join_type']
    assert users[1].is_active == user_data_2['is_active']
    assert users[1].is_block == user_data_2['is_block']
    assert users[1].is_admin == user_data_2['is_admin']


async def test_user_login(app, create_user, repository: UserPGRepository):
    user = await repository.user_login(
        email=user_data_1['email'],
        password=user_data_1['password'],
        join_type=user_data_1['join_type']
    )
    assert isinstance(user, UserEntity) is True
