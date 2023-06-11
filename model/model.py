import json


class Book:

    def __init__(self, book_id, isbn, title, author, publication_date):
        self.book_id = book_id
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_date = publication_date


__first_free_id = 1
__books = []


def __load_db():
    global __first_free_id
    with open('books.json', encoding='utf-8') as mock_books:
        books: dict = json.load(mock_books)

        for book in books:
            b = Book(int(book['id']), book['isbn'], book['title'], book['author'], book['publicationDate'])
            __first_free_id += 1
            __books.append(b)

def find_all():
    return __books.copy()

def add_new_book(isbn, title, author, date):
    global  __first_free_id
    __books.append(Book(__first_free_id, isbn, title, author, date))
    __first_free_id += 1


__load_db()

print(__books)
