# This file defines the database schema

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from app import db, login

class User(UserMixin, db.Model):
    """
    This represents the User table that we'll be creating to hold the app users. 
    
    The UserMixin class holds the three state variables that must be present for flask_login. 
    They are: 
    1. is_authenticated - (bool) whether the user has valid credentials
    2. is_active        - (bool) whether the user's account is active 
    3. is_anonymous     - (bool) only True when the user is anonymous
    4. get_id()         - (method) returns a UID for the user as a string
    """

    ADMIN = db.Column(db.Integer, default=0)                        # Define whether the user is an admin or not
    id = db.Column(db.Integer, primary_key=True)                    # The primary key ('id') for the records
    username = db.Column(db.String(64), index=True, unique=True)    # Define the username
    email = db.Column(db.String(120), index=True, unique=True)      # Define the email address
    password_hash = db.Column(db.String(128))                       # Define the password hash
    #isCustomer = db.Column(db.bool, default=False)                  # Whether or not the user is a customer   

    def __repr__(self):
        """
        How this class should show itself
        """
        return 'User: {}'.format(self.username)

    def set_password(self, password):
        """
        Generating the password hash
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Tests the given password against the stored password hash
        """
        return check_password_hash(self.password_hash, password)

class Customer(db.Model):
    """
    Represents the individual customers
    """
    id = db.Column(db.Integer, primary_key=True)                            # The primary key ('id') for the records
    firstname = db.Column(db.String(64), index=True, unique=False)          # Customer's first name
    middleinit = db.Column(db.String(1), index=True, unique=False)          # Middle initial
    lastname = db.Column(db.String(64), index=True, unique=False)           # Customer's last name
    address1 = db.Column(db.String(64), index=True, unique=False)           # Address Line 1
    address2 = db.Column(db.String(64), index=True, unique=False)           # Address Line 2
    city = db.Column(db.String(64), index=True, unique=False)               # City
    state = db.Column(db.String(64), index=True, unique=False)              # State
    postal  = db.Column(db.Integer, index=True, unique=False)               # Postal Code
    phone = db.Column(db.String(64), index=True, unique=True)               # Phone number
    email = db.Column(db.String(120), index=True, unique=True)              # Define the email address
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)   # The date of the customer's creation

    def __repr__(self):
        """
        How this class should show itself
        """
        return 'Customer ID: {}, Customer Name:{}, {}'.format(self.id, self.lastname, self.firstname)

@login.user_loader                  # Allows us to pass the load_user function to flask_login's user_loader function
def load_user(id):                  # This loads a specific user - acts as an interface between the db and flask_login
    return User.query.get(int(id))  # A simple query to get the user object based on the id