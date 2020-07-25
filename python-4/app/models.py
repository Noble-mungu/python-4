from .import db
from werkzeug.security import generate_password
from flask_login import UserMixin
from .import login_manager
from datetime import datetime

@login_manager.user_loader


def load_user(user_id):
	return user.query.get(int(user_id))

class User(UserMixin):

     

    def __repr__(self):
     	return f'User{self.username}'




