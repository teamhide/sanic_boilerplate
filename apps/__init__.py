from sanic import Sanic
from apps.users.views import bp as user_bp
from gino.ext.sanic import Gino


def create_app():
    app = Sanic(__name__)
    app.blueprint(user_bp)
    db = Gino()
    db.init_app(app)
    return app
