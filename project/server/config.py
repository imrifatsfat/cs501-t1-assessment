import os
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = 'sqlite:///'
database_name = 'diagnostic'


class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'diagnostic_secret')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = DATABASE_URL + database_name


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = DATABASE_URL + database_name + '_test.db'
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'diagnostic_secret'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://vpxwwjaixcnncd:52c36cb157a587633f89c6f6d68e59d6b94f2505195c62cb89f703ced7abc106@ec2-34-228-154-153.compute-1.amazonaws.com:5432/d4tsrtqnn71jmi'
