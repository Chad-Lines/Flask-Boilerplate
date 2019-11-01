# This file defines the URL routing and contains much of the logic behind the app

from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.forms import LoginForm
from app.models import User
from app import app

@app.route('/')         # Allows us to pass the index() function to the app.route function tied
@app.route('/index')    # to the '/' and '/index' URLs, respectively
@login_required         # Anonymous users will be redirected to the login view per __init__.py Ln. 18
def index():
    """
    Returning the page when a user hits the index route
    """
    return render_template('index.html', title='Home')  # Calls the template and sets the title

                                                
@app.route('/login', methods=['GET', 'POST'])   # Allows us to pass in the login() function tied to the '/login' URL
def login():                                    # NOTE: The 'GET' and 'POST' allow us to handle the flow of data                                                                   
    """                             
    Handles the logic for the login page 
    """
    if current_user.is_authenticated:                                   # If the user is already authenticated (current_user comes from Flask-Login)...
        return redirect(url_for('index'))                               # Just forward them to the index page
    form = LoginForm()                                                  # Defining the form that we're going to render (see forms.py)
    if form.validate_on_submit():                                       # This will do the form processing work. If the browser sends POST, then validate_on_submit() gathers
                                                                        # the data, runs the validators (if defined), and returns True if all is well and good. So here we're
                                                                        # essentially saying "If everything checks out..."
        user = User.query.filter_by(username=form.username.data).first()# Query the User table for the username provide, then assign to the 'user' variable
        if user is None or not user.check_password(form.password.data): # If the user is not found, or the password does not match...
            flash('Invalid username or password')                       # Alert the user...
            return redirect(url_for('login'))                           # and keep them on the login page
        login_user(user, remember=form.remember_me.data)                # Otherwise, log the user in and determine whether to 'remember' them\
        next_page = request.args.get('next')                            # This will be set if an anonymous user was redirected to the login page from a protected 
                                                                        # page (denoted by '@login_required')
        if not next_page or url_parse(next_page).netloc != '':          # This allows us to check if there was another page that the anonymous user was trying to reach
            next_page = url_for('index')                                # If there was no next_page, then we just send the user to '/index'
        return redirect(next_page)                                      # Redirect the user to the 'next_page' page
    return render_template('login.html', title='Sign In', form=form)    # If the form has not been validated, then render the login template and the form

@app.route('/logout')                   # Allows us to pass in the logout() function tied to the '/logout' URL
def logout():                           # This function is very simple. 
    """
    Logout the user, redirect them to '/index'  
    """ 
    logout_user()                       # Call logout_user() (a function from flask_login) to log the user out of their session
    return redirect(url_for('index'))   # Redirect the user to the index page
