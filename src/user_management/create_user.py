users_db = {}  # This will ideally be a database or a more persistent storage.

def create_new_user(username, password, access_to_docs=False):
    if username not in users_db:
        users_db[username] = {
            "password": password,
            "has_access_to_docs": access_to_docs
        }
        print(f"User {username} created successfully!")
        
        if access_to_docs:
            print("User has been granted access to training materials and documentation.")
    else:
        print(f"User {username} already exists!")

# For demonstration purposes
if __name__ == "__main__":
    create_new_user("alice", "passwordAlice", True)
