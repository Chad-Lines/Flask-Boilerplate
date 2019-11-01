# This file defines the forms that we can display in our site/app

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    """
    This defines the login form
    """
    username = StringField('Username', validators=[DataRequired()])     # Defining the username field
    password = PasswordField('Password', validators=[DataRequired()])   # Defining the password field
    remember_me = BooleanField('Remember Me')                           # Allows user to bypass login in the future
    submit = SubmitField('Sign In')                                     # The button to actually sign in

class RegistrationForm(FlaskForm):
    """
    A form for users to be able to register for accounts
    """
    username = StringField('Username', validators=[DataRequired()])             # The username to use
    email = StringField('Email', validators=[DataRequired(), Email()])          # Email addresss
    password = PasswordField('Password', validators=[DataRequired()])           # Desired password
    password2 = PasswordField(                                                  # Confirming the password
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')                                            # The submission button

    def validate_username(self, username):
        """
        Used to make sure that the user doesn't attempt to use an existing username
        """
        user = User.query.filter_by(username=username.data).first()     # Attempting to query for the username provided
        if user is not None:                                            # If the username is already in use...
            raise ValidationError('That username is already in use.')   # Alert the user

    def validate_email(self, email):
        """
        Used to make sure that the user doesn't attempt to use an existing email
        """
        user = User.query.filter_by(email=email.data).first()           # Attempting to query for the email provided
        if user is not None:                                            # If the email is already in use...
            raise ValidationError('Email address is already in use.')   # Alert the user