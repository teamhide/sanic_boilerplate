class Config:
    HOST = '127.0.0.1'
    PORT = 8000
    DEBUG = True


class DevelopmentConfig(Config):
    HOST = '127.0.0.1'
    PORT = 8000
    DEBUG = True


class ProductionConfig(Config):
    HOST = '0.0.0.0'
    PORT = 8000
    DEBUG = False


class TestingConfig(Config):
    HOST = '127.0.0.1'
    PORT = 8000
    DEBUG = True
