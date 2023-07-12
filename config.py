import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    SECRET_KEY = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = f'mysql://{os.getenv("user")}:{os.getenv("password")}@{os.getenv("host")}:3306/{os.getenv("dbName")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
