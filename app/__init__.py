

# __init__.py — Application Factory
# This script initalizes the Flask ap, database, login manager(session management), and CLI commands.
# It also integrates FLask-Migrate for Alembic-based database migrations.

from flask import Flask
from flask_login import LoginManager        # Authentication sessions
from .models import db, User
from dotenv import load_dotenv
# import for pytest running custom commands
from .custom_commands import register_commands

# Added only for DB migration
from flask_migrate import Migrate
import os
from flask_limtier import Limiter

load_dotenv()   # Load environment variables from .env
login_manager = LoginManager()      # Login configuration
# Added only for DB migration
migrate = Migrate()
limiter = Limiter(get_remote_address)
# Create Flask app instance
def create_app():
    app = Flask(__name__)
    # .env Configuration
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
            "pool_pre_ping": True   # Detects stale connections    
            "pool_recycle": 3600    # Prevent connection timeouts
    }

    # initialize Flask extensions with app
    db.init_app(app)            # SQLAlchemy ORM
    migrate.init_app(app, db)   # Alembic migration management  
    login_manager.init_app(app) # Session and user authentication
    # security login limiter
    limiter.init_app(app)
    form app.routes import main
    app.register_blueprint(main)
    # Configure Flask-Login Behaviour
    login_manager.login_view = "main.login"     # Redirect to this route if user is not logged in 
    login_manager.login_message_category = "info"   # Bootstrap flash message category

    # Register custom CLI commands (e.g., for tests  or setup)
    register_commands(app)

    # Flask-Login user loader: tells flask how to get a user object
    @login_manager.user_loader
    def load_user(user_id):
        try:
            return User.query.get(int(user_id))
        except(ValueError, TypeError):
            return None # handle userid gracefully


    # Register Flask Blueprints for modular routing
    from app.routes import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
