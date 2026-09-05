def test_get_profile_empty(client, auth_headers):
    resp = client.get("/api/v1/profile", headers=auth_headers)
    assert resp.status_code == 200
    assert resp.json() is None


def test_create_and_update_profile(client, auth_headers):
    resp = client.put(
        "/api/v1/profile",
        headers=auth_headers,
        json={"name": "Vikas", "skills": ["python", "aws"], "experience_years": 2},
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["name"] == "Vikas"
    assert body["skills"] == ["python", "aws"]

    resp2 = client.put("/api/v1/profile", headers=auth_headers, json={"name": "Vikas K"})
    assert resp2.status_code == 200
    assert resp2.json()["name"] == "Vikas K"
    assert resp2.json()["skills"] == ["python", "aws"]  # untouched fields persist


def test_profile_requires_auth(client):
    resp = client.get("/api/v1/profile")
    assert resp.status_code == 403
