class Config:
	'''
	parent configuration
	'''
class ProdConfig(config):
	pass

class DevConfig(config):

config_options = {
'develpoment':DevConfig,
'production':ProdConfig
}
