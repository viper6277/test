
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

# This is input in the form of a string
password_provided = "password"

# Convert to type bytes
password = password_provided.encode()

# CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
salt = b'salt_PyFrame'

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once

message = "my deep dark secret".encode()

f = Fernet(key)

encrypted = f.encrypt(message)

print(encrypted.decode())

decrypted = f.decrypt(encrypted)

print(decrypted)