import os


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    ENV = 'dev'


class TestingConfig(BaseConfig):
    TESTING = True
    ENV = 'testing'


class ProductionConfig(BaseConfig):
    DEBUG = False
    ENV = 'prod'


config = {
    'dev': DevelopmentConfig,
    'testing': TestingConfig,
    'prod': ProductionConfig,
    'default': DevelopmentConfig
}

def configure_app(app):
    env = os.getenv('FLASK_CONFIGURATION', 'default')
    if not env in config.keys():
        env = 'default'
    # config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[env])
    app.config.from_pyfile('config.cfg', silent=True)