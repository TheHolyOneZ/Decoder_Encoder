import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

def load_encryption_key():
    """Load the encryption key from the .env file."""
    load_dotenv()
    key = os.getenv("ENCRYPTION_KEY")
    if not key:
        raise ValueError("ENCRYPTION_KEY not found in .env file.")
    return key

def decrypt_credentials(encrypted_username, encrypted_password):
    """Decrypt the encrypted username and password."""
    key = load_encryption_key()
    cipher = Fernet(key.encode())
    decrypted_username = cipher.decrypt(encrypted_username.encode()).decode()
    decrypted_password = cipher.decrypt(encrypted_password.encode()).decode()
    return decrypted_username, decrypted_password

def read_encrypted_file(file_name):
    """Read encrypted credentials from a file."""
    with open(file_name, "r") as file:
        lines = file.readlines()
        encrypted_username = lines[0].strip().split(": ")[1]
        encrypted_password = lines[1].strip().split(": ")[1]
    return encrypted_username, encrypted_password

def decrypt_from_manual_input():
    """Decrypt credentials entered manually."""
    encrypted_username = input("Enter the encrypted username: ")
    encrypted_password = input("Enter the encrypted password: ")
    username, password = decrypt_credentials(encrypted_username, encrypted_password)
    print("\nDecrypted Credentials:")
    print(f"Username: {username}")
    print(f"Password: {password}")

def decrypt_from_file():
    """Decrypt credentials from an encrypted file."""
    input_file = input("Enter the encrypted file name (default: encrypted_credentials.txt): ") or "encrypted_credentials.txt"
    try:
        encrypted_username, encrypted_password = read_encrypted_file(input_file)
        username, password = decrypt_credentials(encrypted_username, encrypted_password)
        print("\nDecrypted Credentials:")
        print(f"Username: {username}")
        print(f"Password: {password}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    """Main function with an option menu to select input method."""
    print("=== Credential Decoder ===")
    print("1: Enter encrypted username and password manually")
    print("2: Load encrypted credentials from a file")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        decrypt_from_manual_input()
    elif choice == "2":
        decrypt_from_file()
    else:
        print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
