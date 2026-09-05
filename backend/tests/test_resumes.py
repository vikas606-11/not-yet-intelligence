import io


def test_upload_resume_pdf(client, auth_headers):
    file_content = b"%PDF-1.4 fake pdf content"
    resp = client.post(
        "/api/v1/resumes",
        headers=auth_headers,
        files={"file": ("resume.pdf", io.BytesIO(file_content), "application/pdf")},
    )
    assert resp.status_code == 201
    assert resp.json()["file_type"] == "pdf"


def test_upload_resume_rejects_bad_type(client, auth_headers):
    resp = client.post(
        "/api/v1/resumes",
        headers=auth_headers,
        files={"file": ("resume.txt", io.BytesIO(b"hello"), "text/plain")},
    )
    assert resp.status_code == 400


def test_list_and_delete_resume(client, auth_headers):
    file_content = b"%PDF-1.4 fake"
    upload = client.post(
        "/api/v1/resumes",
        headers=auth_headers,
        files={"file": ("resume.pdf", io.BytesIO(file_content), "application/pdf")},
    )
    resume_id = upload.json()["id"]

    listed = client.get("/api/v1/resumes", headers=auth_headers)
    assert len(listed.json()) == 1

    deleted = client.delete(f"/api/v1/resumes/{resume_id}", headers=auth_headers)
    assert deleted.status_code == 204

    listed_after = client.get("/api/v1/resumes", headers=auth_headers)
    assert len(listed_after.json()) == 0
