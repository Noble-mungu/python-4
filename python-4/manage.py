from app import create_app
from flask_script import Manager,Server
# from app.models import User


app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server(host='localhost',port=1234))

@manager.add_command
def test():
	import unittest
	tests = unittest.TestLoader().discover('test')
	unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
		manager.run()

