import pytest
from flask_login import login_user
from app.modules.auth.models import User

pytestmark = pytest.mark.integration


def test_notepad_index_requires_login(test_client):
    response = test_client.get("/notepad", follow_redirects=False)
    assert response.status_code in (302, 303)
    assert "/login" in response.headers["Location"]


def test_notepad_index_responds(test_client):
    user = User.query.filter_by(email="user1@example.com").first()
    with test_client.session_transaction() as session:
        session["_user_id"] = str(user.id)
        session["_fresh"] = True

    response = test_client.get("/notepad")
    assert response.status_code == 200, f"/notepad did not return 200 (got {response.status_code})"