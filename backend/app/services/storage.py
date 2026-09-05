"""
Local-disk resume storage for Phase 1.

Swap this module for an S3-backed implementation later (Phase 3+/cloud phases)
without changing any caller — the interface (save, url_for) stays the same.
"""
import os
import uuid

from app.core.config import settings


def _ensure_dir() -> None:
    os.makedirs(settings.resume_storage_dir, exist_ok=True)


def save_resume(user_id: str, filename: str, content: bytes) -> str:
    _ensure_dir()
    ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else "bin"
    key = f"{user_id}_{uuid.uuid4().hex}.{ext}"
    path = os.path.join(settings.resume_storage_dir, key)
    with open(path, "wb") as f:
        f.write(content)
    return path


def delete_resume(file_url: str) -> None:
    if os.path.exists(file_url):
        os.remove(file_url)
