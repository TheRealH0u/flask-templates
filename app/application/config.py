from application.util import generate
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'WLIXBKQrE4uNoBGf5bvdACmKQMNzPjrkwSpqnkwODH0ShIcOW0Zt2y9WspsCxaiL'
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Strict'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.normpath(f'{basedir}/../database.db')

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
