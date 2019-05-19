from sanic import Sanic
from apps.users.views import bp as user_bp


def create_app():
    app = Sanic(__name__)
    app.blueprint(user_bp)
    return app
