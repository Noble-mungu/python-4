from flask_script import Manager,Server
from app import create_app
from flask_migrate import Migrate,MigrateCommand
from app.models import User
app = create_app()

manager = Manager(app)
manager.add_command('server',Server(use_debugger=True))
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
	return dict(app = app ,db = db,User = User)

@manager.add_command
def test():
	import unittest
	test = unittest.TestLoader().discover('test')
	unittest.TxtTestRunner(verbosity=2).run(tests)



if __name__ == '__main__':
	manager()