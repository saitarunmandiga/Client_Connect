# This will ideally be a database or a more persistent storage. Assuming users_db exists for demonstration.
users_db = {
    "alice": {
        "password": "passwordAlice",  # Ideally this should be a hashed password, not plain text
        "has_access_to_docs": True
    }
}

def authenticate(username, password):
    user = users_db.get(username)
    if user and user['password'] == password:
        return True
    return False

# For demonstration purposes
if __name__ == "__main__":
    print(authenticate("alice", "passwordAlice"))  # This should return True
