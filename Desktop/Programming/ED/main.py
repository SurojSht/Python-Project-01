from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a key for encryption and decryption.
    Save this key securely and don't lose it.
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as 'secret.key'")

def load_key():
    """
    Loads the key from the current directory named `secret.key`.
    """
    return open("secret.key", "rb").read()

def encrypt_message(message: str) -> bytes:
    """
    Encrypts a message using the key.
    
    :param message: The message to encrypt.
    :return: The encrypted message.
    """
    key = load_key()
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message: bytes) -> str:
    """
    Decrypts an encrypted message using the key.
    
    :param encrypted_message: The encrypted message to decrypt.
    :return: The decrypted message.
    """
    key = load_key()
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

if __name__ == "__main__":
    print("1. Generate a new key")
    print("2. Encrypt a message")
    print("3. Decrypt a message")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        generate_key()
    elif choice == "2":
        message = input("Enter the message to encrypt: ")
        encrypted = encrypt_message(message)
        print(f"Encrypted message: {encrypted}")
    elif choice == "3":
        encrypted_message = input("Enter the message to decrypt: ").encode()
        decrypted = decrypt_message(encrypted_message)
        print(f"Decrypted message: {decrypted}")
    else:
        print("Invalid choice! Please select 1, 2, or 3.")
