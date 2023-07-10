from app import app, db, socket
from app.model import User, Msg

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Msg': Msg}