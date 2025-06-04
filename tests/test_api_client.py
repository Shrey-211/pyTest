# test_api_client.py
import pytest
from unittest.mock import patch
from api_client import get_user, get_posts_by_user

# Sample fake data to use in mocks
FAKE_USER = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz"
}

FAKE_POSTS = [
    {"userId": 1, "id": 1, "title": "Post 1", "body": "Body 1"},
    {"userId": 1, "id": 2, "title": "Post 2", "body": "Body 2"},
]

@patch('api_client.requests.get')
def test_get_user(mock_get):
    # Configure the mock to return a response with our fake user data
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = FAKE_USER

    user = get_user(1)

    # Verify the mock was called with the correct URL
    mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/users/1")

    # Assert the returned data matches our fake data
    assert user == FAKE_USER

@patch('api_client.requests.get')
def test_get_posts_by_user(mock_get):
    # Setup mock response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = FAKE_POSTS

    posts = get_posts_by_user(1)

    mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/posts", params={"userId": 1})

    assert posts == FAKE_POSTS
