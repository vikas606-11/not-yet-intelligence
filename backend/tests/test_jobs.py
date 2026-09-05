def _create_job(client, auth_headers):
    return client.post(
        "/api/v1/jobs",
        headers=auth_headers,
        json={"title": "DevOps Engineer", "company": "Acme", "description": "Manage CI/CD and cloud infra."},
    )


def test_create_job(client, auth_headers):
    resp = _create_job(client, auth_headers)
    assert resp.status_code == 201
    assert resp.json()["title"] == "DevOps Engineer"
    assert resp.json()["source"] == "manual"


def test_list_jobs(client, auth_headers):
    _create_job(client, auth_headers)
    resp = client.get("/api/v1/jobs")
    assert resp.status_code == 200
    assert len(resp.json()) == 1


def test_get_job_not_found(client):
    resp = client.get("/api/v1/jobs/does-not-exist")
    assert resp.status_code == 404


def test_save_job_and_list_saved(client, auth_headers):
    job_id = _create_job(client, auth_headers).json()["id"]

    resp = client.post(f"/api/v1/jobs/{job_id}/save", headers=auth_headers)
    assert resp.status_code == 201
    assert resp.json()["status"] == "saved"

    # saving again is idempotent, not a duplicate row
    resp2 = client.post(f"/api/v1/jobs/{job_id}/save", headers=auth_headers)
    assert resp2.status_code == 201

    saved = client.get("/api/v1/jobs/saved", headers=auth_headers)
    assert len(saved.json()) == 1
