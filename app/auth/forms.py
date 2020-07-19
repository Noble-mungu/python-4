from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField,PasswordField,SubmitField,BooleanFiield
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class LoginFrom(FlaskForm):
     username = StringField('Username',validators=[Required()])
    password = passwordField('password',validators=[Required()])
    remember = BooleanField('Remember Me!')
    submit = submitField('Login')

class RegForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(),Email()])
    username = StringField('Enter Your Username', validators=[Required()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')
    def valid_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('An account with that email already exist')

    def validate_email(self,data_field)
    if User.query.filter_by(email = data_field.data).first():
        raise valiadationError ("The Email has already been taken")


    def valid_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('The username you entered has already been taken'