from app.models import User, db

def test_user_created_in_db(client, app):

    client.post("/register", data={
        "username": "testuserdb",
        "email": "testuserdb@mail.com",
        "password": "testpassdb",
        "confirm_password": "testpassdb"
        }, follow_redirects=True)

    with app.app_context():
        user = User.query.filter_by(email="testuserdb@mail.com").first()
        assert user is not None
        assert user.username =="testuserdb"
