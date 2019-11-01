# This file contains the configuration options for the app

import os

basedir = os.path.abspath(os.path.dirname(__file__))    # Getting the working path

class Config(object):
    SECRET_KEY = 'Passw0rd'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'crm.db')    # Setting the path  to the database file
    SQLALCHEMY_TRACK_MODIFICATIONS = False                                      # This disables automatic signaling on modifications