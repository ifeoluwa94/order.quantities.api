from os import environ, path


class Config:
    """Set app_main base configuration from application_secrets.json file."""
    # General Config
    SECRET_KEY = ''  # environ.get('SECRET_KEY')
    FLASK_APP = ''  # environ.get('FLASK_APP')
    FLASK_ENV = ''  # environ.get('FLASK_ENV')


class ProdConfig(Config):
    """Set app_main production configuration."""
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    """Set app_main development configuration."""
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
