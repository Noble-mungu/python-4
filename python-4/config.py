class Config:
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY=os.environ.get('SECRET_KEY')
class ProdConfig(Config):
	pass

class DevConfig(Config):
	'''
	DEvelopment configuaration
	'''





config_options = {
'develpoment':DevConfig,
'production':ProdConfig
}
