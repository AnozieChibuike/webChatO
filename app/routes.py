from app import app, db, socket
from flask import request, flash, session, redirect, url_for
from flask import render_template as rd
from app.model import User, Msg
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')



@app.route('/')
@app.route('/home')
def home():
    return rd("index.html.jinja")

@app.route('/signup',methods=["POST","GET"])
def signup():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if User.query.filter_by(email=email).first() is None and User.query.filter_by(username=username).first() is None:
            user = User(username=username,email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return redirect('/login')
        else:
            flash('User exists!')
            return redirect('/signup')
    return rd("signup.html.jinja")

@app.route('/login',methods=['POST','GET'])
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
        login_user(user,remember=remember)
        next_page = request.args.get('next')
        session['welcome'] = f'{current_user.username} joined the chat'
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('chatbox')
        return redirect(next_page)
        
        
        
        
    return rd("login.html.jinja")
    
@socket.on('message')
def message(message):
    socket.send(message)



@app.route('/chatbox',methods=['POST','GET'])
@login_required
def chatbox():
    
    return rd("chat.html")
