# First time run only, creates the database model
# If PostgreSQL Permission errors: run  'docker compose down -v && docker compose up --build'
from app import create_app 
from app.models import db
app = create_app()
with app.app_context():
    db.create_all()
