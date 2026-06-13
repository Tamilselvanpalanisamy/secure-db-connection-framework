from password_utils import encrypt_password  
from cryptography.fernet import Fernet


# Generate a key and save to File
def generate_key():
    key = Fernet.generate_key()
    with open("secret", "wb") as f:
        f.write(key)
    print(f"Key generated and saved to secret")

if __name__ == "__main__":
    # Uncomment this only for first time
    generate_key()

    # Replace with your mysql root password
    encrypted = encrypt_password("@Ponytail0302")
    print("Encrypted password (copy this to your mysql_connect_safe.py):")
    print(encrypted)