#######
# Filename: routes.py
# Summary: Retrieves form data, queries the user, and Executes/calls the user.check_password(...) function. 
#######

# Flask and DB imports for easy template rendering & handling visitors and registered members. 
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user, login_required
from app.models import db, User
from app.forms import RegistrationForm, LoginForm
from flask import current_app as app

# Create the Blueprint
main = Blueprint('main', __name__)

# Defining Root Route
@main.route('/')
def home():
    return render_template('home.html')

# Define Registration Route
@main.route('/register', methods=['GET', 'POST'])
# registration function
def register():
    # Only Allow Access to Dashboard by Authenticated Users
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    form = RegistrationForm()
    if form.validate_on_submit():

        existing_user = User.query.filter_by(email=form.email.data).first()
        # Check if registration email already exists in DB
        if existing_user:
            flash("Email is already Registered, try loggin in or using a different email", 'danger')
            return render_template('register.html', form=form)
        existing_email = User.query.filter_by(email=form.email.data).first()
        existing_username = User.query.filter_by(username=form.username.data).first()

        # Check if registration email already exists in DB
        if existing_email:
            flash("Email is already Registered, Please Log in or use a different email", 'danger')
            return render_template('register.html', form=form)
        if existing_username:
            flash("Username is already taken. Please Choose a Different one.", 'danger')
            return render_template('register.html', form=form)

        # Create new user
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created! You may now Login.', 'success')
        return redirect(url_for('main.login'))

    return render_template('register.html', form=form)

# Define Login  Route
@main.route('/login', methods=["GET", "POST"])
def login():
    # check if user is authenticated
    if current_user.is_authenticated:
        print(f"User Exists: {user}")
        print(f"Authenticated: {current_user.is_authenticated}")
        return redirect(url_for('main.dashboard'))

    # Initialize the LoginForm
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash(f'Successfully Logged in as: {current_user.username} ', 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('Login Failed. Check email/password', 'danger')
    return render_template('login.html', form=form)

# Define DashBoard Route
@main.route('/dashboard')
@login_required
def dashboard():
    print(f"User Authenticated: {current_user.is_authenticated}, ID: {current_user.id}")
    return render_template('dashboard.html', name=current_user.username)

# Define Logout Route
@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.login'))
