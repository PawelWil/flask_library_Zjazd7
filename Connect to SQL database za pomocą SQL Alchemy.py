#w pliku .env bedzie haslo wykorzystywane
#to połączenie sobie muszę obejrzeć na filmiku + zrobić osobny projekt na Flask SQL ALchemy, żeby to połączenie i setup zrobić.
# Bo na filmiku, ta apka app.py, gdzie było robione wszystko pod tą bazę danych z książkami, została nadpisana przez app.py pod połączenie z SQL Alchemy

# db - to jest instancja łączenia SQL Alechmy


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()