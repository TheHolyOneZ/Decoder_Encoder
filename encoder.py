import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

def load_encryption_key():
    """Load or generate the encryption key."""
    load_dotenv()
    key = os.getenv("ENCRYPTION_KEY")
    if not key:
        key = Fernet.generate_key().decode()
        with open(".env", "a") as env_file:
            env_file.write(f"ENCRYPTION_KEY={key}\n")
    return key

def encrypt_credentials(username, password):
    """Encrypt the username and password."""
    key = load_encryption_key()
    cipher = Fernet(key.encode())
    encrypted_username = cipher.encrypt(username.encode()).decode()
    encrypted_password = cipher.encrypt(password.encode()).decode()
    return encrypted_username, encrypted_password

def save_encrypted_credentials(file_name, username, password):
    """Save the encrypted credentials to a file."""
    encrypted_username, encrypted_password = encrypt_credentials(username, password)
    with open(file_name, "w") as file:
        file.write(f"Encrypted Username: {encrypted_username}\n")
        file.write(f"Encrypted Password: {encrypted_password}\n")

def main():
    """Main function to collect input and save encrypted credentials."""
    print("=== Credential Encoder - TheZ ===")
    username = input("Enter username: ")
    password = input("Enter password: ")
    output_file = input("Enter output file name (default: encrypted_credentials.txt): ") or "encrypted_credentials.txt"

    save_encrypted_credentials(output_file, username, password)
    print(f"Encrypted credentials saved to {output_file}.")

if __name__ == "__main__":
    main()
