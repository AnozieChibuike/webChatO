import sqlite3

connectDb = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connectDb.executescript(f.read())

cur = connectDb.cursor()

cur.execute("INSERT INTO users (username,pass) VALUES (?,?)",
            ('admin','admin'))

connectDb.commit()
connectDb.close()

msgDb = sqlite3.connect('messages.db')

with open('msg.sql') as t:
    msgDb.executescript(t.read())

cr = msgDb.cursor()

cr.execute("INSERT INTO msg (messages) VALUES (?)",('admin : HELLO',))

msgDb.commit()
msgDb.close()
