from flask import Flask
app=Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../blog.db'
app.config['SECRET_KEY'] ='asmpoahs;fjcq[apsdjmqa'
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
from blog import route
