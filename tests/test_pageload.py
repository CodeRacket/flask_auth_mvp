print("Testing webpage response status")
def test_register_page_loads(client):
    response = client.get("/register")
    assert response.status_code == 200
    assert b"register" in response.data.lower()

def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"/" in response.data.lower()

def test_login_page_loads(client):
    response = client.get("login")
    assert response.status_code == 200
    assert b"login" in response.data.lower()
