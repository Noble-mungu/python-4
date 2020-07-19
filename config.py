import os

class Config:


    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:azbycx567@localhost/pitch'

    SQLALCHEMY_TRACK_MODIFICATIONS=True
    # SECRET_KEY=os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    '''
    Production class 
    '''


class DevConfig(Config):

    DEBUG = True
config_options = {
'development' :DevConfig,
'production':ProdConfig
}
