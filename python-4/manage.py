from app import create_app,db
from flask_script import Manager,Server
from app.models import User


app = create_app()

manager = Manager(app)
manager.add_command('server',Server(use_debugger=True))

@manager.add_command
def test():
	import unittest
	tests = unittest.TestLoader().discover('test')
	unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
		manager.run()

