from app import app, db, socket
from flask_socketio import disconnect
from flask import request, flash, session, redirect, url_for
from flask import render_template as rd
from app.model import User, Msg
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

def get_admin_info():
    info = User.query.filter_by(username='info').first()
    if info:
        return info
    else:
        info = User(username='info')
        db.session.add(info)
        db.session.commit()
        info = User.query.filter_by(username='info').first()
        return info

@app.route('/logout')
def logout():
    username = current_user.username
    message = f'{username} left the chat.'
    info = get_admin_info()
    p = Msg(body=message, author=info)
    db.session.add(p)
    db.session.commit()
    socket.emit('mes', {'user': 'info', 'msg': message})
    logout_user()
    return redirect('/')


@app.route('/')
@app.route('/home')
def home():
    return rd("index.html.jinja")


# @socket.on('join')
# def join(data):
#     username = data['username']
#     message = f'{username} joined the chat.'
#     socket.emit('mes', {'user': 'info', 'msg': message})
#     info = get_admin_info()
#     p = Msg(body=message, author=info)
#     db.session.add(p)
#     db.session.commit()
    


# @socket.on('disconnect')
# def leave():
#     info = get_admin_info()
#     username = current_user.username
#     message = f'{username} left the chat.'
#     p = Msg(body=message, author=info)
#     db.session.add(p)
#     db.session.commit()
#     socket.emit('mes', {'user': 'info', 'msg': message})
    



@app.route('/signup', methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if User.query.filter_by(email=email).first() is None and User.query.filter_by(username=username).first() is None:
            user = User(username=username, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return redirect('/login')
        else:
            flash('User exists!')
            return redirect('/signup')
    return rd("signup.html.jinja")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect('/chatbox')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = bool(request.form.get('remember-me'))
        user = User.query.filter_by(email=email).first()
        if user is None or not user.check_password(password):
            flash('Invalid login details')
            return redirect('/login')
        login_user(user, remember=remember)
        next_page = request.args.get('next')
        message = f'{user.username} joined the chat.'
        socket.emit('mes', {'user': 'info', 'msg': message})
        info = get_admin_info()
        p = Msg(body=message, author=info)
        db.session.add(p)
        db.session.commit()
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('chatbox')
        return redirect(next_page)
    return rd("login.html.jinja")


# Handling socket frontend
@socket.on('message')
def message(message):
    u = current_user
    p = Msg(body=message, author=u)
    db.session.add(p)
    db.session.commit()
    socket.emit('mes', {'user': u.username, 'msg': message})


@app.route('/chatbox', methods=['POST', 'GET'])
@login_required
def chatbox():
    posts = Msg.query.all()
    return rd("chat.html", posts=posts)
