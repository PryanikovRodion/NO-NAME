import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from source.saler import Saler
from source.buyer import Buyer
from source.product import Product
from source.magazin import Magazin
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "_---_"

if __name__ == '__main__':
    app.run(debug=True)


