from unittest.mock import Mock, patch

from app import create_app


def test_successful_submission_redirects_to_success_page():
    app = create_app()
    response_mock = Mock(ok=True)
    with patch("app.requests.post", return_value=response_mock):
        response = app.test_client().post("/submit", data={"name": "Asha", "email": "asha@example.com", "course": "DevOps"})
    assert response.status_code == 302
    assert response.headers["Location"].endswith("/success")


def test_backend_error_is_displayed_on_same_page():
    app = create_app()
    response_mock = Mock(ok=False, text="")
    response_mock.json.return_value = {"error": "Database submission failed"}
    with patch("app.requests.post", return_value=response_mock):
        response = app.test_client().post("/submit", data={"name": "Asha", "email": "asha@example.com", "course": "DevOps"})
    assert response.status_code == 400
    assert b"Database submission failed" in response.data
    assert response.request.path == "/submit"
