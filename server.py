from flask import Flask, request, flash, redirect, url_for
from flask import render_template as render
from flask_socketio import SocketIO
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jlskdf'
socketio = SocketIO(app, cors_allowed_origins="*")


def get_db_connection():
    conect = sqlite3.connect('database.db') 
    conect.row_factory = sqlite3.Row
    return conect

def get_msg_db():
    conectMsg = sqlite3.connect('messages.db')
    conectMsg.row_factory = sqlite3.Row
    return conectMsg

@app.route('/')
def index():
    return render('index.html.jinja')


@app.route('/signup', methods=('GET', 'POST'))
def signup():
    if request.method == "GET":
        return render('signup.html.jinja')
    if request.method == 'POST':
        user = request.form['username']
        passW = request.form['pass']
        conn = get_db_connection()
        cursor = conn.cursor()
        if passW == request.form['pass-repeat'] and len(passW) in range(6, 21):
            try:
                cursor.execute('INSERT INTO users (username,pass) VALUES(?,?)',(user,passW))
                conn.commit()
                conn.close()
                return render('success.html')
            except sqlite3.IntegrityError:
                flash('User exists try another username')
                return redirect('/signup')
        if passW != request.form['pass-repeat']:
            flash('Password must be the same')
            return redirect('/signup')
        if len(passW) not in range(6, 21):
            flash('Password less than 6 characters or greater than 20 characters')
            return redirect('/signup')
    
@socketio.on('message')
def handle_message(message):
    print('Client-side message : ' + message)
    con = get_msg_db()
    cur = con.cursor()
    cur.execute('insert into msg (messages) values(?)',(message,))
    con.commit()
    con.close()
    socketio.send(message)

@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'GET':
        return render('login.html.jinja')
    elif request.method == 'POST':
        user = request.form['username']
        passW = request.form['pass']
        conn = get_db_connection()
        cursor = conn.cursor()
        con = get_msg_db()
        cur = con.cursor()
    
        if cursor.execute('select * from users where username = ? and pass = ?',(user,passW)).fetchone() != None:
            rt = cursor.execute('select * from users where username = ? and pass = ?',(user,passW)).fetchone()['username']
            con = get_msg_db()
            cur = con.cursor()
            show = cur.execute('select * from msg').fetchall()
            return render('chat.html',rt=rt,show=show)
        else:
            flash('Password or Username Incorrect')
            return redirect(url_for('login'))
    

@app.route('/donate')
def donate():
    return render('donate.html.jinja')

if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0',allow_unsafe_werkzeug=True)
