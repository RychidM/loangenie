
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

secrete_key = os.environ.get('SECRETE_KEY')

app = Flask(__name__)

app.config['SECRET_KEY'] = secrete_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loangenie.db'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from loangenie import routes

if __name__ == "__main__":
    app.run()