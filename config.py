import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'Testing Server'
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir,'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
