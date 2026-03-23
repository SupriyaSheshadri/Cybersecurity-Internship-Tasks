#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os

print(os.path.exists("testfile.txt"))


# In[1]:


import os

if os.path.exists("stored_hash.txt"):
    os.remove("stored_hash.txt")
    print("Old hash file deleted")
else:
    print("No stored hash file found")


# In[2]:


import hashlib
import os

print("=== File Integrity Checker ===")

# Function to calculate hash of the file
def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()


# Function to store hash
def store_hash(hash_value):
    with open("stored_hash.txt", "w") as f:
        f.write(hash_value)


# Function to read stored hash
def read_hash():
    if os.path.exists("stored_hash.txt"):
        with open("stored_hash.txt", "r") as f:
            return f.read()
    return None


# File to monitor
file_path = "testfile.txt"

print("Checking file:", file_path)

# Calculate current hash
current_hash = calculate_hash(file_path)

# Read stored hash
stored_hash = read_hash()

# Compare hashes
if stored_hash is None:
    print("No previous hash found.")
    store_hash(current_hash)
    print("Hash stored for future comparison.")

elif current_hash == stored_hash:
    print("File integrity maintained. No changes detected.")

else:
    print("WARNING: File has been modified!")

print("=== Scan Complete ===")


# In[3]:


import hashlib
import os

print("=== File Integrity Checker ===")

# Function to calculate hash of the file
def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()


# Function to store hash
def store_hash(hash_value):
    with open("stored_hash.txt", "w") as f:
        f.write(hash_value)


# Function to read stored hash
def read_hash():
    if os.path.exists("stored_hash.txt"):
        with open("stored_hash.txt", "r") as f:
            return f.read()
    return None


# File to monitor
file_path = "testfile.txt"

print("Checking file:", file_path)

# Calculate current hash
current_hash = calculate_hash(file_path)

# Read stored hash
stored_hash = read_hash()

# Compare hashes
if stored_hash is None:
    print("No previous hash found.")
    store_hash(current_hash)
    print("Hash stored for future comparison.")

elif current_hash == stored_hash:
    print("File integrity maintained. No changes detected.")

else:
    print("WARNING: File has been modified!")

print("=== Scan Complete ===")


# In[4]:


import hashlib
import os

print("=== File Integrity Checker ===")

# Function to calculate hash of the file
def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()


# Function to store hash
def store_hash(hash_value):
    with open("stored_hash.txt", "w") as f:
        f.write(hash_value)


# Function to read stored hash
def read_hash():
    if os.path.exists("stored_hash.txt"):
        with open("stored_hash.txt", "r") as f:
            return f.read()
    return None


# File to monitor
file_path = "testfile.txt"

print("Checking file:", file_path)

# Calculate current hash
current_hash = calculate_hash(file_path)

# Read stored hash
stored_hash = read_hash()

# Compare hashes
if stored_hash is None:
    print("No previous hash found.")
    store_hash(current_hash)
    print("Hash stored for future comparison.")

elif current_hash == stored_hash:
    print("File integrity maintained. No changes detected.")

else:
    print("WARNING: File has been modified!")

print("=== Scan Complete ===")


# In[ ]:




