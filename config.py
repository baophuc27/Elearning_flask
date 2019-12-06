class Config(object):
    pass


class DevelopmentConfig(Config):

    DEBUG = True
    TESTING=True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY="HELLO"


class ProductionConfig(Config):
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}