from sanic import Blueprint
from core.databases import db
from core.config import get_connection, IS_DOCKER


events = Blueprint('events')


@events.listener('before_server_start')
async def setup_connection(app, loop):
    config = get_connection()
    if IS_DOCKER == 'true':
        await db.set_bind(f"postgresql+asyncpg://sanic:sanic@db:5432/sanic")
    else:
        await db.set_bind(f"postgresql+asyncpg://{config.DB_HOST}/{config.DB_NAME}")
