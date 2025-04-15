import shelve
import sys
import os
import atexit
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from source.saler import Saler
from source.buyer import Buyer
from source.product import Product
from source.magazin import Magazin
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '/web/app')))
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
filename = 'web/store'

# Создаем папку, если её нет
#os.makedirs(os.path.dirname(filename), exist_ok=True)

# Открываем shelve-файл
with shelve.open(filename) as dbs:
    if 'store' in dbs:
        store = dbs['store']
        print("Загружена структура из файла:")
    else:
        store = Magazin("store",[],[])
        dbs['store'] = store
        print("Создана новая структура и сохранена:")

    print(store)

from app import routes,models

def save_store():
    with shelve.open(filename) as dba:
        dba["store"] = store

atexit.register(save_store)



