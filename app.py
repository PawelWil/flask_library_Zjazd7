#dokumentacja UIkit
# link: https://getuikit.com/docs/table



from flask import Flask, render_template, request, redirect, url_for, abort
from model import model

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/books')
def all_books():
    return render_template('books.html', books=model.find_all())

@app.route('/books/add', methods=['GET', 'POST'])
def add_book():
    if request.method =='GET':
        return render_template('add_books.html')

    #jeśli nie GET, musi być POST
    new_book_data = request.form
    model.add_new_book(
        new_book_data['isbn'],
        new_book_data['title'],
        new_book_data['author'],
        new_book_data['date']
    )
    return redirect(url_for('all_books'))

@app.route('/books/<int:book_id>')
def find_book_by_id(booki_id: int)
    found_book = model.find_by_id(booki_id)

    if not found_book:
        abort(404, f"Nie znaleziono ksiązki po id {booki_id}")



if __name__ == '__main__':
    app.run()
