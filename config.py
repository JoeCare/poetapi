import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    CSRF_ENABLED = False
    CSRF_SESSION_KEY = os.getenv('CSRF_SESSION_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SESSION_COOKIE_NAME = os.getenv('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_ECHO = True
    CSRF_ENABLED = True
    JSONIFY_PRETTYPRINT_REGULAR = True
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    # Special for Heroku:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL').replace(
        "://", "ql://", 1)


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_ECHO = False
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    # SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        BASE_DIR, 'app.db')
