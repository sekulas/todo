from asyncore import file_dispatcher
from flask import Flask # Zalaczamy jedna klase
from flask_sqlalchemy import SQLAlchemy
import os #'standardowa' biblioteka

file_path = os.path.abspath(os.getcwd()) + "/todo.db" #Przypisujemy sciezke do zmiennej (cwd - to curently working directory) (abspath - znormalizowana sciezka - doprowadza do obecnego folderu cala sciezke)

app = Flask(__name__) #"__name__" <- teraz to jest __init.py__
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path #adres do bazy danych do configu, sqlite protokół bazy danych, przez ten protokół baza w chumerze bedzie komunikowala sie z naszym kompem
db = SQLAlchemy(app) #pokazujemy bazie danych jaka aplikacja z niej korzysta, tworzymy baze danych

from app import routes #moduł kolejny ze ścieżkami strony internetowej



#https://www.mongodb.com/languages/python