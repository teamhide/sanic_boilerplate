import pytest
from core.databases import db
from core.config import TestingConfig


@pytest.fixture
async def app():
    return await db.set_bind(f'postgresql://{TestingConfig.DB_HOST}/{TestingConfig.DB_DATABASE}')
