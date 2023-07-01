from app import app, db
from flask import request, flash, session, redirect
from flask import render_template as rd
from app.model import User, Msg


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
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = bool(request.form.get('remember-me'))
        return remember
    return rd("login.html.jinja")
