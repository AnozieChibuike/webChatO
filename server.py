from flask import Flask, request, flash, redirect, jsonify, url_for
from flask import render_template as render
from csv import writer
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jlskdf'
socketio = SocketIO(app, cors_allowed_origins="*")

id = 0
rt = ''
users = [{'user': 'admin', 'pass': 'admin', 'id': id}]


@app.route('/')
def index():
    return render('index.html.jinja')


@app.route('/signup', methods=('GET', 'POST'))
def signup():
    global id
    global users
    if request.method == 'POST':
        user = request.form['username']
        passW = request.form['pass']
        if passW == request.form['pass-repeat'] and len(passW) in range(6, 21):
            if not any(user in d.values() for d in users):
                id += 1
                users.append({'user': user, 'pass': passW, 'id': id})
                with open('data.csv','w',encoding='utf8',newline='') as c:
                    write = writer(c)
                    header = ['ID','USERNAME','PASSWORD']
                    write.writerow(header)
                    for i in users: 
                        write.writerow([i['id'],i['user'],i['pass']])
                return render('success.html', id=id, user=user, passW=passW)
            elif any(user in d.values() for d in users):
                flash('User exists try another username')
                return redirect('/signup')
        if passW != request.form['pass-repeat']:
            flash('Password must be the same')
            return redirect('/signup')
        if len(passW) not in range(6, 21):
            flash('Password less than 6 characters or greater than 20 characters')
            return redirect('/signup')
    if request.method == "GET":
        return render('signup.html.jinja')


@app.route('/login', methods=('GET', 'POST'))
def login():
    global users
    global rt
    if request.method == 'GET':
        return render('login.html.jinja', users=users)
    elif request.method == 'POST':
        user = request.form['username']
        passW = request.form['pass']
        idL = int(request.form['id'])
        try:
            data = users[idL]
            if user == data['user'] and passW == data['pass']:
                rt = data['user']
                return render('chat.html',rt=rt)
            else:
                flash('Password or Username Incorrect')
                return redirect(url_for('login'))
            
        except IndexError:
            flash("Id does not exists or incorrect id for user")
            return redirect(url_for('login'))
    

@socketio.on('message')
def handle_message(message):
    print('Client-side message : ' + message)
    
    socketio.send(message)
@app.route('/donate')
def donate():
    return render('donate.html.jinja')



if __name__ == '__main__':
    socketio.run(app,host="127.0.0.1")
