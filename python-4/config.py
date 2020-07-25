class Config:
	'''
	parent configuration
	'''
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
