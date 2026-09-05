def test_register_success(client):
    resp = client.post("/api/v1/auth/register", json={"email": "a@example.com", "password": "password123"})
    assert resp.status_code == 201
    assert resp.json()["email"] == "a@example.com"


def test_register_duplicate_email(client):
    client.post("/api/v1/auth/register", json={"email": "a@example.com", "password": "password123"})
    resp = client.post("/api/v1/auth/register", json={"email": "a@example.com", "password": "password123"})
    assert resp.status_code == 400


def test_register_short_password_rejected(client):
    resp = client.post("/api/v1/auth/register", json={"email": "a@example.com", "password": "short"})
    assert resp.status_code == 422


def test_login_success(client):
    client.post("/api/v1/auth/register", json={"email": "a@example.com", "password": "password123"})
    resp = client.post("/api/v1/auth/login", json={"email": "a@example.com", "password": "password123"})
    assert resp.status_code == 200
    assert "access_token" in resp.json()


def test_login_wrong_password(client):
    client.post("/api/v1/auth/register", json={"email": "a@example.com", "password": "password123"})
    resp = client.post("/api/v1/auth/login", json={"email": "a@example.com", "password": "wrongpass"})
    assert resp.status_code == 401


def test_me_requires_auth(client):
    resp = client.get("/api/v1/auth/me")
    assert resp.status_code == 403  # no bearer token supplied


def test_me_with_valid_token(client, auth_headers):
    resp = client.get("/api/v1/auth/me", headers=auth_headers)
    assert resp.status_code == 200
    assert resp.json()["email"] == "test@example.com"
