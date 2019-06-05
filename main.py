import os
from sanic import Sanic
from apps import create_app


if __name__ == '__main__':
    env = os.getenv('SANIC_CONFIG', 'develop')
    app: Sanic = create_app()
    app.run(host='0.0.0.0', port=8000, debug=True, workers=os.cpu_count() if env == 'production' else 1)
