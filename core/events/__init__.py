from sanic import Blueprint
from core.databases import db


events = Blueprint('events')


@events.listener('before_server_start')
async def setup_connection(app, loop):
    await db.set_bind(f"postgresql+asyncpg://{app.config['DB_HOST']}/{app.config['DB_NAME']}")
