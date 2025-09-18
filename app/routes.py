#######
# Filename: routes.py
# Summary: Retrieves form data, queries the user,
# and Executes/calls the user.check_password(...) function.
#######

# Flask and DB imports—for easy template
# handling for visitors and registered members.
from flask import Blueprint, render_template, redirect, url_for, flash, jsonify

# from flask import request
from flask_login import login_user, current_user, logout_user, login_required
from app.models import db, User
from app.forms import RegistrationForm, LoginForm
# User sanitization escape all user input little bobby 'drop tables.
from markupsafe import escape
from sqlalchemy.exc import IntegrityError   # avoid NameError
import logging
# import limiter from __init__.py 
from app import limiter 
# for production set basicConfig to level=logging.INFO
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
# from flask import current_app as app

# Create the Blueprint
main = Blueprint("main", __name__)


# Defining Root Route
@main.route("/")
def home():
    return render_template("home.html")


# Define Registration Route
@main.route("/register", methods=["GET", "POST"])
@limiter.limit("5 per minute")
# registration function
def register():
    # Only Allow Access to Dashboard by Authenticated Users
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))
    form = RegistrationForm()
    if form.validate_on_submit():
        # Check if registration email and username already exists in DB
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        try:
            db.session.commit()
            flash("Account created! You may now login.", "success")
            return redirect(url_for("main.login"))
        # Catches relational DB violations
        except IntegrityError:  
            db.session.rollback()
            flash("Email or username already exists. Please try again.", "danger")
        except Exception as e:
            db.session.rollback()
            flash(f"Registration failed. Please try again.", "danger")
            #includes the stack trace in logs for better debugging.
            logging.error(f"Registration error: {str(e)}", exc_info=True)
        return render_template("register.html", form=form)

    else:
        if form.errors:
            logging.debug(f"Form validation errors: {form.errors}")
           
        return render_template("register.html", form=form)
 
# implement limiter for login protection

# Define Login  Route
@main.route("/login", methods=["GET", "POST"])
@limiter.limit("5 per minute")
def login():
    # check if user is authenticated
    if current_user.is_authenticated:
        # proper way to handle debugging 
        logging.debug(f"User exists: {current_user}")
        return redirect(url_for("main.dashboard"))

    # Initialize the LoginForm
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            # XSS protection markupsafe escape
            flash(f"Successfully Logged in as: {escape(current_user.username)}", "success")
            return redirect(url_for("main.dashboard"))
        else:
            flash("Login Failed. Check email/password", "danger")
    return render_template("login.html", form=form)


# Define DashBoard Route
@main.route("/dashboard")
@login_required
def dashboard():
    logging.debug(f"User Authenticated: {current_user.is_authenticated}, ID: {current_user.id}")
    return render_template("dashboard.html", name=escape(current_user.username))


# Define Logout Route
@main.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("main.login"))
    
    
@main.route("/health")
def health_check():
    # might have to update the string search for the health check unit test ...
    return jsonify({"status":"OK"}), 200

