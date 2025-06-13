# Used for simplifying pytohn app testing
import pytest
# import flask_auth_mvp  app factory
from app import create_app 
# import the db  instance
from app.models import db

# Create a fresh app for testing
@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "WTF_CSRF_ENABLED": False, #disable CSRF for tests
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()
