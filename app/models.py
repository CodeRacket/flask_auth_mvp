#################
# CodeRacket
# File: models.py
# Summary: models.py
# Defines the User class with logic for
# checking the hashed password securely.
################

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

# Provides trusted hash functions that store and check passwords safely.
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # below—Complains the string exceeded buffer, 128 bytes or chars
    # password_hash = db.Column(db.String(128), nullable=False)
    password_hash = db.Column(db.Text, nullable=False)

    # Hashes the Password before stroing into DB
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Password Validation against the stored hash
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
