import pyotp

# Create a secret key for the user (generate this securely and associate it with the user)
def create_secret_key():
    secret_key = pyotp.random_base32()
    return secret_key

# Enable multi-factor authentication for a user
def enable_mfa(user_id):
    secret_key = create_secret_key()
    # Store the secret_key securely in the user's profile or database record
    user_data[user_id]['secret_key'] = secret_key
    user_data[user_id]['mfa_enabled'] = True

# Disable multi-factor authentication for a user
def disable_mfa(user_id):
    # Remove the secret_key and disable MFA for the user
    user_data[user_id]['secret_key'] = None
    user_data[user_id]['mfa_enabled'] = False

# Verify a TOTP code
def verify_totp(user_id, totp_code):
    secret_key = user_data[user_id].get('secret_key')
    if secret_key:
        totp = pyotp.TOTP(secret_key)
        return totp.verify(totp_code)
    return False

if __name__ == "__main__":
    # Simulated user data (in practice, store this in a database)
    user_data = {
        'alice': {'password': 'passwordAlice', 'mfa_enabled': False, 'secret_key': None},
    }

    # User registration and enabling MFA (optional)
    user_id = 'alice'
    enable_mfa(user_id)

    # Simulated login process
    username = 'alice'
    password = 'passwordAlice'
    provided_totp_code = '123456'  # This code is obtained from the user

    if username in user_data:
        user = user_data[username]
        if user['password'] == password:
            if user['mfa_enabled']:
                if verify_totp(username, provided_totp_code):
                    print("Login successful with MFA.")
                else:
                    print("Invalid TOTP code. Login failed.")
            else:
                print("Login successful without MFA.")
        else:
            print("Incorrect password. Login failed.")
    else:
        print("User not found. Login failed.")
