from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ad66d90a56b675248acb31307cca3cc8017fc2ac'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///C:/Users/bittu/Desktop/EkChhat/EkChhat/test.db"
app.config['SQLAlCHEMY_TRACK_MODIFICATION'] = True
db = SQLAlchemy(app)

from mainapp import routes



