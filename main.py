import os
from sanic import Sanic
from apps import create_app


SANIC_CONFIG = os.getenv('SANIC_CONFIG', 'development')
app = Sanic(__name__)


if __name__ == '__main__':
    app: Sanic = create_app()
    app.run(host='0.0.0.0', port=8000, debug=True)
