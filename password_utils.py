from cryptography.fernet import Fernet

# Class to prevent accidental printing of password
class Fakestr(str):
    def __str__(self):
        return "****"
    def __repr__(self):
        return "****"

# Load the secret key from file using absolute path
def load_key():
    return open("secret", "rb").read()

# Encrypt the plain password using the secret key
def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode())

# Decrypt the encrypted password and return the protected password
def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_password).decode()
    return Fakestr(decrypted)
 
# Final method to call from app
def get_decrypted_password():
    encrypted_password = b'gAAAAABqLP_DYe13liz6taHWatRs3HxpHhm2K0HMmo8wEVPEMCWpIsS3P0-FVIX1X4R2dGIIVshf0sZZEz3hKVtHq7TFHA18ZQ=='
    D = decrypt_password(encrypted_password)
    return D