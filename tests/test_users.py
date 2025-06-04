import requests
import pytest

def test_get_users(base_url):
    res = requests.get(f"{base_url}/users?page=2")
    assert res.status_code == 200
    assert res.json()["page"] == 2

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user_by_id(base_url, user_id):
    res = requests.get(f"{base_url}/users/{user_id}")
    assert res.status_code == 200
    assert res.json()["data"]["id"] == user_id
