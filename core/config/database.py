import os


IS_DOCKER = os.getenv('IS_DOCKER', 'false')


class Config:
    DB_HOST = '127.0.0.1'
    DB_DATABASE = 'sanic'
    DB_USER = 'sanic'
    DB_PASSWORD = 'sanic'


class DevelopmentConfig(Config):
    if IS_DOCKER == 'true':
        DB_HOST = 'db'
    else:
        DB_HOST = '127.0.0.1'
    DB_DATABASE = 'sanic'
    DB_USER = 'sanic'
    DB_PASSWORD = 'sanic'


class ProductionConfig(Config):
    DB_HOST = '127.0.0.1'
    DB_DATABASE = 'sanic'
    DB_USER = 'sanic'
    DB_PASSWORD = 'sanic'


class TestingConfig(Config):
    DB_HOST = '127.0.0.1'
    DB_DATABASE = 'sanic'
    DB_USER = 'sanic'
    DB_PASSWORD = 'sanic'


def get_connection():
    config_type = os.getenv('SANIC_CONFIG', 'development')
    if config_type == 'production':
        return ProductionConfig()
    elif config_type == 'testing':
        return TestingConfig()
    else:
        return DevelopmentConfig()
