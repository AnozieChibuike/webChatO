from app import app
from flask import render_template as rd
@app.route('/')
@app.route('/home')
def home():
    return rd("index.html.jinja")

