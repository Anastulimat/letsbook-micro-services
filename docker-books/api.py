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
    return '''<h1>This is the BOOKS Rest API</h1>
<p>Connect to one of the followings (mind the URL, how it's formed):<br>
    <a href="./api/v1/resources/books/all">Catalog</a><br>
    <a href="./api/v1/resources/books?published=2000">Books published in 2000</a><br>
    <a href="./api/v1/resources/books?author=Jo Walton">Books by Jo Walton</a><br>
</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM books;').fetchall()
    return jsonify(all_books)

  
@app.route('/api/v1/resources/add/', methods=['POST'])
def add_book():
    author = request.form.get('author')
    published = request.form.get('published')
    book_id = request.form.get('id')
    title = request.form.get('title')
    first_sentence = request.form.get('first_sentence')

    if (title is None):
        print("Aborting - author is None")
        return jsonify("Error - You need to post at least a title")
    
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('insert into books (author, published, id, title, first_sentence) values (?,?,?,?,?);', (author,published, book_id, title, first_sentence,))
    conn.commit()
    return jsonify("Done")



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/resources/books', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')

    query = "SELECT * FROM books WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)
    if not (id or published or author):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

if __name__ == "__main__":
    app.run("0.0.0.0", port=8000, debug=True)
