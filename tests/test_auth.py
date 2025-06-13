def test_valid_registration(client):
    print("Registration test running ...")
    response = client.post("/register", data={
        "username": "testuser",
        "email": "testuser@mail.com",
        "password": "password123",
        "confirm_password": "password123"
        }, follow_redirects=True)

    assert response.status_code == 200
    assert b"login" in response.data.lower()

def test_invalid_login(client):
    print("Testing invalid login")
    # Register first
    client.post("/register", data={
            "username": "testuser2", 
            "email": "testuser2@mail.com",
            "password": "password123",
            "confirm_password": "password123"
            })
    response = client.post("/login", data={
        "email": "testuser2@mail.com",
        "password": "wrongpass"
        }, follow_redirects=True)
    assert b"login failed" in response.data.lower() 

def test_valid_login(client):
    response = client.post("/register", data={
        "username": "testuser3", 
        "email": "testuser3@mail.com",
        "password": "testpass3",
        "confirm_password": "testpass3"
        })

    response=client.post("/login", data={
        "email": "testuser3@mail.com",
        "password": "testpass3"
        }, follow_redirects=True)

    assert response.status_code == 200
    assert b"dashboard" in response.data.lower() or b"successfully logged in as" in response.data.lower()

def test_logout(client):
    print("Testing user logout function")

    client.post("/register", data={
        "username": "testuser4",
        "email": "testuser4@mail.com",
        "password": "testpass4",
        "confirm_password": "testpass4"
        }, follow_redirects=True)

    client.post("login", data={
        "email": "testuser42mail.com",
        "password": "tespass4"
        }, follow_redirects=True)

    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200
    assert b"login" in response.data.lower() or b"logged out" in response.data.lower()

def test_dashboard_requires_login(client):
    print("Testing: dashboard requires login")
    response = client.get("/dashboard", follow_redirects=True)
    assert response.status_code == 200
    assert b"login" in response.data.lower() or b"please log in" in response.data.lower()
