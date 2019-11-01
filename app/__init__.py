# This file builds the app

from flask import Flask, session
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)           # Creates the flask application. __name__ is set to the name of the module
                                # in which is is used, i.e. "crm" via crm.py
app.config.from_object(Config)  # Getting the app configuration from the Config object (see config.py)
db = SQLAlchemy(app)            # This object represents the database (see notes.txt for explanation)
migrate = Migrate(app, db)      # This object represents the migration engine (see notes.txt for explanation)
login = LoginManager(app)       # This object represents the login manager (see notes.txt for explanation)
login.login_view = 'login'      # By providing this view, we can elsewhere dictate what anonymous users can see vs. logged-in users

from app import routes, models  # 'routes' handles routing and 'models' defines the database schema

#from app.models import User
#from app.model_views import AdminPage

# admin = Admin(app, name='Administration', index_view=AdminPage())
#admin.add_view(ModelView(User, db.session))