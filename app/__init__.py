from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_socketio import SocketIO

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
login = LoginManager(app)
login.login_view = 'login'
socket = SocketIO(app, cors_allowed_origin="*")

from app import routes,model

