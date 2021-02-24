import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
# app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>This is the NOTES Rest API</h1>
<p>Connect to one of the followings (mind the URL, how it's formed):<br>
    <a href="./api/v1/resources/notes/all">All Notes on all books</a><br>
    <a href="./api/v1/resources/notes?user_id=1">Notes by user 1</a><br>
    <a href="./api/v1/resources/notes?book_id=2">Notes on book 2</a><br>
</p>'''


@app.route('/api/v1/resources/notes/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('notes.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_notes = cur.execute('SELECT * FROM notes;').fetchall()
    return jsonify(all_notes)

  
@app.route('/api/v1/resources/add/', methods=['POST'])
def add_book():
    note = request.form.get('note')
    user_id = request.form.get('user_id')
    book_id = request.form.get('book_id')
    if (user_id is None or book_id is None or note is None):
        print("Aborting - Missing info")
        return jsonify("Error - To call this REST API, you need to give a note, a user_id and a book_id")
    
    conn = sqlite3.connect('notes.db')
    cur = conn.cursor()
    cur.execute('insert into notes (book_id, user_id, note) values (?,?,?);', (book_id, user_id, note,))
    conn.commit()
    return jsonify("Done")



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/resources/notes', methods=['GET'])
def api_filter():
    query_parameters = request.args

    book_id = query_parameters.get('book_id')
    user_id = query_parameters.get('user_id')

    query = "SELECT * FROM notes WHERE"
    to_filter = []

    if book_id:
        query += ' book_id=? AND'
        to_filter.append(book_id)
    if user_id:
        query += ' user_id=? AND'
        to_filter.append(user_id)
    if not (book_id or user_id):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('notes.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

if __name__ == "__main__":
    app.run("0.0.0.0", port=8080, debug=True)
