from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

#DATABASE = '/Users/tejaswath/Desktop/Build_something/bookstore-app/shared/bookstore.db'
#DATABASE = os.environ.get('DATABASE', '/app/shared/bookstore.db')
DATABASE = '/app/shared/bookstore.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/books', methods=['POST'])
def add_book():
    book = request.json
    title = book.get('title')
    author = book.get('author')

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Book added!', 'book': book}), 201

@app.route('/books', methods=['GET'])
def get_books():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM books')
    books = c.fetchall()
    conn.close()

    books_list = [{'id': row[0], 'title': row[1], 'author': row[2]} for row in books]
    return jsonify({'books': books_list}), 200

if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        init_db()
    app.run(host='0.0.0.0', port=5001)