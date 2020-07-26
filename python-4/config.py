import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:azbycx567@localhost/blogworld'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='wertyuiokjhvxcvbn'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    DEBUG = True