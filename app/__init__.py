from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from config import SQLALCHEMY_DATABASE_URI
app = Flask(__name__)

app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.environ['SECRET']
db = SQLAlchemy(app)
engine = db.create_engine(SQLALCHEMY_DATABASE_URI)
db.create_all(engine)
from app import views, models