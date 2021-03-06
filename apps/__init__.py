from sanic import Sanic
from apps.users.views import bp as user_bp
from apps.home import bp as home_bp
from core.config import get_connection
from core.databases import db


def create_app():
    app = Sanic(__name__)
    config = get_connection()
    app.config.from_object(config)
    app.blueprint(user_bp)
    app.blueprint(home_bp)
    db.init_app(app)
    return app
