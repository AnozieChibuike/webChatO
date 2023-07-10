import os

class Config(object):
    SECRET_KEY = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = f'mysql://{os.getenv("username")}:{os.getenv("password")}@{os.getenv("host")}/{os.getenv("dbName")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
