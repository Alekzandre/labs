import os


class Config:
    SECRET_KEY = 'secret_key'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ECHO = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://<username>:<pass>@<host>/<db>'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://<username>:<pass>@<host>/<db>'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://<username>:<pass>@<host>/<db>'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
