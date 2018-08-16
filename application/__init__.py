# flask-sovellus
from flask import Flask
app = Flask(__name__)


#jos postgreSQL käytössä, yhdistetään siihen. Muutoin yhdistetään paikallisesti sqlLiteen
from flask_sqlalchemy import SQLAlchemy
import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///questions.db"    
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)


# toiminnallisuudet
from application import views

from application.questions import models
from application.questions import views

from application.auth import models
from application.auth import views

from application.answers import models
from application.answers import views

from application.courses import models

# kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# tietokantataulut tarvittaessa
try:
    db.create_all()
except:
    pass


