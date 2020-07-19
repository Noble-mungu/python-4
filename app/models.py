from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user


class User(UserMixin,db.Model):

    """ 
    class modelling the users 
    """

    __tablename__='users'

    #create the columns
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index =True)
    secure_password = db.Column(db.String(255),nullable = False)
    bio = db.Column(db.String(255))
    #profile_pic = db.Column(db.String())

    @property
    def set_password(self):
        raise AttributeError('You cannot read the password attribute')

    @set_password.setter
    def password(self, password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.secure_password,password) 
    
    def save_u(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __table__ ='pitches'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255),nullable = False)
    post = db.Column(db.Text(),nullable = False)
    comment = db.relationship('Comment',backref='pitch',lazy='dynamic')
    upvote = db.relationship('Comment',backref='pitch',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='pitch'lazy='dynamic')
    user_id = db.Column(db.Integer,db.ForeigKey('users.id'))
    time = db.Column(db.DateTime, default = datetime.utcnow)
    category = db.Column(db.String(255), index = True,nullable = False)
    
    def save_p(self):
        db.session.add(self)
        db.session.commit()
    def __repr__(self):
        return f'pitch {self.post}'
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text(),nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'),nullable = False)

    def save_c(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,pitch_id):
        comments = Comment.query.filter_by(pitch_id=pitch_id).all()

        return comments

    
    def __repr__(self):
        return f'comment:{self.comment}'

  
@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)