# auth/auth_utils.py
import json
import hashlib

def load_users():
    """
    Load user credentials from a JSON file.
    Format contoh data/users.json:
    {
      "admin": "<sha256-hash dr password>"
    }
    """
    try:
        with open("data/users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def hash_password(password: str) -> str:
    """
    Hash password using SHA256.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username: str, password: str) -> bool:
    """
    Check if username and password are correct.
    """
    users = load_users()
    hashed_pass = hash_password(password)

    # Cek apakah username ada di data, dan password-nya cocok
    if username in users and users[username] == hashed_pass:
        return True
    return False
