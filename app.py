#dokumentacja UIkit
# link: https://getuikit.com/docs/table

#dokumentacja Blueprint. 'Blueprint' służy do rozdzielania funkcjonalności z glównej aplikacji, żeby kod był bardziej przejrzysty
# link: https://flask.palletsprojects.com/en/2.3.x/blueprints/

#Flask SQL ALchemy - za pomocą Flask SQL Alchemy, Flask może łączyć się z bazą danych SQl. Ale wazne, instaluje Flask SQL Alchemy, a nie SQL Alchemy!
# db - to jest instancja łączenia SQL Alechmy

#w pliku .env bedzie haslo wykorzystywane
#to połączenie sobie muszę obejrzeć na filmiku + zrobić osobny projekt na Flask SQL ALchemy, żeby to połączenie i setup zrobić.
# Bo na filmiku, ta apka app.py, gdzie było robione wszystko pod tą bazę danych z książkami, została nadpisana przez app.py pod połączenie z SQL Alchemy

# czyli będą dwa projekty, jedno związane bezpośrednio z bazą danych ksiązek (projekt ma być przesłany przez p.Andrzeja na githuba),
# + nowy projekt który będzie miał dokładnie wszystko to samo, oprócz oczywiście app.py i zmian, które sobie przepiszę oglądając filmik
# to jest ostatni filmik z dnia 11.06.

#ważne też, żeby wszystkie te pliki HTMLa i pozostałe związane z bazą danych książek zostawić, bo na czymś trzeba pracować





from flask import Flask, render_template, request, redirect, url_for, abort
from model import model

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/books')
def all_books():
    query_params = request.args
    title = query_params.get('filter_name')
    all_books = model.find_all()

    if title:
        filtered = []
        for book in all_books:
            if title.casefold() in book.title.casefold():
                filtered.append(book)
        return render_template('books.html', books=filtered)
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
def find_book_by_id(book_id: int):
    found_book = model.find_by_id(book_id)

    if not found_book:
        abort(404, f"Nie znaleziono ksiązki po id {book_id}")

    return render_template('book.html', book=found_book)

@app.route ('/books/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id: int):
    model.delete_book(book_id)
    return redirect(url_for('all_books'))




if __name__ == '__main__':
    app.run()
