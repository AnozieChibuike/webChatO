import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'Testing Server'
    SQLALCHEMY_DATABASE_URI = f'mysql://sql6631717:Cyam9hdema@sql6.freesqldatabase.com/sql6631717'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
