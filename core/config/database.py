import os


IS_DOCKER = os.getenv('IS_DOCKER', 'false')


class Config:
    DB_HOST = 'sanic:sanic@127.0.0.1:5432'
    DB_NAME = 'sanic'
    DB_PASS = 'sanic'


class DevelopmentConfig(Config):
    if IS_DOCKER == 'true':
        DB_HOST = 'sanic:sanic@db:5432'
    else:
        DB_HOST = 'sanic@127.0.0.1:5432'
    DB_NAME = 'sanic'
    DB_PASS = 'sanic'


class ProductionConfig(Config):
    DB_HOST = 'sanic:sanic@127.0.0.1:5432'
    DB_NAME = 'sanic'
    DB_PASS = 'sanic'


class TestingConfig(Config):
    DB_HOST = 'sanic:sanic@127.0.0.1:5432'
    DB_NAME = 'sanic'
    DB_PASS = 'sanic'


def get_connection():
    config_type = os.getenv('SANIC_CONFIG', 'development')
    if config_type == 'production':
        return ProductionConfig()
    elif config_type == 'testing':
        return TestingConfig()
    else:
        return DevelopmentConfig()
