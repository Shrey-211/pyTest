import requests

def test_login_success(base_url):
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    res = requests.post(f"{base_url}/login", json=payload)
    assert res.status_code == 200
    assert "token" in res.json()

def test_login_failure_missing_password(base_url):
    payload = {"email": "eve.holt@reqres.in"}
    res = requests.post(f"{base_url}/login", json=payload)
    assert res.status_code == 400
    assert res.json()["error"] == "Missing password"
