# api_client.py
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_user(user_id):
    """Fetch user details from dummy API."""
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    response.raise_for_status()
    return response.json()

def get_posts_by_user(user_id):
    """Fetch posts made by the user."""
    response = requests.get(f"{BASE_URL}/posts", params={"userId": user_id})
    response.raise_for_status()
    return response.json()

# Example usage
if __name__ == "__main__":
    user = get_user(1)
    print("User:", user)

    posts = get_posts_by_user(1)
    print("Posts by User 1:", posts)