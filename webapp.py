from flask import Flask
import os

if "ISHEROKU" in os.environ:
    running_on_heroku = True
    
app = Flask(__name__)

if running_on_heroku:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:aaa@localhost/flaskapp'
    

from views import *

if __name__ == '__main__':
    app.debug = True
    print("running")
    app.run()
