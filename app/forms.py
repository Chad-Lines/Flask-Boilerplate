# This file defines the forms that we can display in our site/app

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    """
    This defines the login form
    """
    username = StringField('Username', validators=[DataRequired()])     # Defining the username field
    password = PasswordField('Password', validators=[DataRequired()])   # Defining the password field
    remember_me = BooleanField('Remember Me')                           # Allows user to bypass login in the future
    submit = SubmitField('Sign In')                                     # The button to actually sign in