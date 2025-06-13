# Used for simplifying pytohn app testing
import pytest
# import flask_auth_mvp  app factory
from app import create_app 
# import the db  instance
from app.models import db as _db

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
        _db.create_all()
        yield app
        _db.session.remove()
        _db.drop_all()

@pytest.fixture(scope="function")
def client(app):
    return app.test_client()

@pytest.fixture(scope="function")
def runner(app):
    return app.test_cli_runner
