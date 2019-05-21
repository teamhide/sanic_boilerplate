import os


class Config:
    DB_HOST = 'sanic@127.0.0.1:5432'
    DB_NAME = 'sanic'


class DevelopmentConfig(Config):
    DB_HOST = 'sanic@127.0.0.1:5432'
    DB_NAME = 'sanic'


class ProductionConfig(Config):
    DB_HOST = 'sanic@127.0.0.1:5432'
    DB_NAME = 'sanic'


class TestingConfig(Config):
    DB_HOST = 'sanic@127.0.0.1:5432'
    DB_NAME = 'sanic'


def get_connection():
    config_type = os.getenv('SANIC_CONFIG', 'development')
    if config_type == 'production':
        return ProductionConfig()
    elif config_type == 'testing':
        return TestingConfig()
    else:
        return DevelopmentConfig()
