from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'Python',
        'author': 'Guido Van Rossum'
    },
    {
        'id': 2,
        'title': 'Java',
        'author': 'James Gosling'
    }
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    for index, book in enumerate(books):
        if book.get('id') == id:
            return book

@app.route('/books', methods=['POST'])
def add_new_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(books)

@app.route('/books/<int:id>', methods=['PUT'])
def update_books(id):
    new_book = request.get_json()
    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index] = new_book
    return jsonify(books)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_books(id):
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]
    return jsonify(books)

app.run(port=5000, host='localhost', debug=True)