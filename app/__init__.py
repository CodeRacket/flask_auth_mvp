# Python __init__ script used by run.py
# Handles  App Creation, Importing User Database Schema,
# Secure handling of Session Key
from flask import Flask
from flask_login import LoginManager
from .models import db, User
from dotenv import load_dotenv
# import for pytest running custom commands
from .custom_commands import register_commands

# Added only for DB migration
from flask_migrate import Migrate
import os

load_dotenv()
login_manager = LoginManager()
# Added only for DB migration
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Configure Login Behaviour
    login_manager.login_view = "main.login"
    login_manager.login_message_category = "info"

    register_commands(app)

    # User Loaded Callback: Flask-Login needs this
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Required to Load @main.route
    from app.routes import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
