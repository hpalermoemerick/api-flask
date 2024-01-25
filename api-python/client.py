import requests

# received books - GET
received_books = requests.get('http://localhost:5000/books').json()
print('received books\n', received_books)

# received a book - GET
received_a_book = requests.get('http://localhost:5000/books/1').json()
print('received books\n', received_a_book)

# make a book
new_book = {
    'id': 3,
    'title': 'JavaScript',
    'author': 'Brendan Eich'
}
received_books = requests.post("http://localhost:5000/books", json=new_book).json()
print('received books\n', received_books)

# update a book
new_book = {
    'id': 1,
    'title': 'Language Programming Python',
    'author': 'Brendan Eich'
}
received_books = requests.put("http://localhost:5000/books/1", json=new_book).json()
print('received books\n', received_books)

# delete a book
received_books = requests.delete("http://localhost:5000/books/2").json()
print('received books\n', received_books)