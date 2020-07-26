from flask import Flask 
from config import Config
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
bootstap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from .auth import auth as authentication_blueprint
    from .main import main as main_blueprint

    app.register_blueprint(authentication_blueprint)
    app.register_blueprint(main_blueprint)

    login_manager.init_app(app)
    db.init_app(app)
    bootstap.init_app(app)
    mail.init_app(app)
    
    return app

    