#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install cryptography')


# In[1]:


from cryptography.fernet import Fernet
import os

# Generate key if not exists
def generate_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)

# Load key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt message
def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted

# Decrypt message
def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_message).decode()
    return decrypted


print("=== Encryption Tool ===")

generate_key()

message = input("Enter message to encrypt: ")

encrypted_msg = encrypt_message(message)
print("Encrypted message:", encrypted_msg)

decrypted_msg = decrypt_message(encrypted_msg)
print("Decrypted message:", decrypted_msg)


# In[ ]:




