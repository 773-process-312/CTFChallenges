import os
import sqlite3
from flask import Flask, render_template, request, redirect, g

app = Flask(__name__)
DATABASE = os.environ['DATABASE']

# Boilerplate to work with a sqlite DB
# Stolen from:
# http://flask.pocoo.org/docs/1.0/patterns/sqlite3/
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# * Our code. *

@app.route('/note/<int:note_id>')
def get_note(note_id):
    # Query the database.
    result = query_db(
        'select * from notes where ROWID = ?',
        [note_id],
        one=True
    )
    if result is None:
        content = 'Note not found'
    else:
        content = result[0]

    data = {
        'id': note_id,
        'contents': content
    }

    return render_template('note.html', data=data)


@app.route('/add', methods=['POST'])
def add_note():
    query = 'insert into notes (content) values (?)'
    db = get_db()
    res = db.execute(query, (request.form['paste'],))
    row_id = res.lastrowid
    db.commit()
    res.close()
    return redirect("/note/%i" % row_id)

@app.route('/')
def index_root():
    return render_template('index.html')
