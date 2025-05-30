#Python __init__ script used by run.py
# Handles  App Creation, Importing User Database Schema, Secure handling of Session Key
# 
from flask import Flask
from flask_login import LoginManager
from .models import db, User
from dotenv import load_dotenv
import os
load_dotenv()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    # initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Configure Login Behaviour
    login_manager.login_view = 'main.login'
    login_manager.login_message_category = 'info'

    # User Loaded Callback: Flask-Login needs this
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    # Register the Routes!
    from app.routes import main as main_blueprint # Required to Load @main.route
    app.register_blueprint(main_blueprint)
    
    return app


