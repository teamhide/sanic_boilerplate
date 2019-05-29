import pytest
from core.databases import db
from core.config import TestingConfig


@pytest.fixture
async def app():
    await db.set_bind(f'postgresql://{TestingConfig.DB_HOST}/{TestingConfig.DB_DATABASE}')
    yield await db.gino.create_all()
    await db.gino.drop_all()
    await db.pop_bind().close()
