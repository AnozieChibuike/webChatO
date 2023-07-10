from app import app, db, socket
from app.model import User, Msg

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Msg': Msg}

if __name__ == '__main__':
    socket.run(app,allow_unsafe_werkzeug=True,host='0.0.0.0')