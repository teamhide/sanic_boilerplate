import os
from dataclasses import dataclass


IS_DOCKER = os.getenv('IS_DOCKER', 'false')


@dataclass(frozen=True)
class Config:
    DB_HOST: str = os.getenv('DB_HOST', '127.0.0.1')
    DB_DATABASE: str = os.getenv('DB_DATABASE', 'sanic')
    DB_USER: str = os.getenv('DB_USER', 'sanic')
    DB_PASSWORD: str = os.getenv('DB_PASSWORD', 'sanic')


@dataclass(frozen=True)
class DevelopmentConfig(Config):
    if IS_DOCKER == 'true':
        DB_HOST: str = 'db'
    DB_DATABASE: str = 'develop'
    DEBUG: bool = True


@dataclass(frozen=True)
class ProductionConfig(Config):
    DEBUG: bool = False


@dataclass(frozen=True)
class TestingConfig(Config):
    DB_DATABASE: str = 'test'
    DEBUG: bool = True


def get_connection():
    config_type = os.getenv('SANIC_CONFIG', 'development')
    if config_type == 'production':
        return ProductionConfig()
    elif config_type == 'testing':
        return TestingConfig()
    else:
        return DevelopmentConfig()
