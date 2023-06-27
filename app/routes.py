from app import app
from flask import render_template as rd

@app.route('/')
@app.route('/home')
def home():
    return rd("index.html.jinja")

@app.route('/signup')
def signup():
    return rd("signup.html.jinja")

@app.route('/login')
def login():
    return rd("login.html.jinja")
