from flask import Flask
from app import app,db, store
from app.models import User



@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}




