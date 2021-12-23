from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '27b0383374a7ff7dd68ced9eff4cc352'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) # initialize database
bcrypt = Bcrypt(app) # hashed passwords
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info' # this is a bootstrap class to change the look of the message

# need to import the routes at the bottom to avoid circular references. Must be after db creation
from flaskblog import routes