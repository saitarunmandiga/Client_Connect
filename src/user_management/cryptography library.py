from cryptography.fernet import Fernet

# Generate a random encryption key (do this once and store it securely)
def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

# Load the encryption key from a secure location
def load_key():
    return open("encryption_key.key", "rb").read()

# Encrypt customer data
def encrypt_data(data, encryption_key):
    cipher_suite = Fernet(encryption_key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

# Decrypt customer data
def decrypt_data(encrypted_data, encryption_key):
    cipher_suite = Fernet(encryption_key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data.decode()

if __name__ == "__main__":
    # Generate and store the encryption key securely (do this once)
    generate_key()

    # Load the encryption key
    key = load_key()

    # Sample customer data
    customer_data = "Customer Name: Alice, SSN: 123-45-6789, Credit Card: 1234-5678-9876-5432"
    
    # Encrypt customer data
    encrypted_customer_data = encrypt_data(customer_data, key)
    print("Encrypted Data:", encrypted_customer_data)

    # Decrypt customer data (for authorized access)
    decrypted_customer_data = decrypt_data(encrypted_customer_data, key)
    print("Decrypted Data:", decrypted_customer_data)
