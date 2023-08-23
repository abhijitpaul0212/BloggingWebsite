# This file maintains all project level configurations
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False
    DEBUG_TB_ENABLED = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_SALT = 'my_precious_two'
    
    # mail settings
    MAIL_SERVER = os.environ.get('APP_MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('APP_MAIL_PORT', 465))
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    # gmail authentication
    # MAIL_USERNAME = os.environ['APP_MAIL_USERNAME']
    # MAIL_PASSWORD = os.environ['APP_MAIL_PASSWORD']
    MAIL_USERNAME = "abhijitpaul0212@gmail.com"
    MAIL_PASSWORD = "agcnachbdlgvvdjy"

    # mail accounts
    MAIL_DEFAULT_SENDER = 'abhijitpaul0212@gmail.com'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance/app.db')
    DEBUG_TB_ENABLED = True
    