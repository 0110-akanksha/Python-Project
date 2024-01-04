import sqlite3
from cryptography.fernet import Fernet

# Function to generate a key
def generate_key():
    return Fernet.generate_key()

# Function to encrypt data
def encrypt_data(data, key):
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data

# Function to decrypt data
def decrypt_data(encrypted_data, key):
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data).decode()
    return decrypted_data

# Generate a key (you should keep this key secure)
encryption_key = generate_key()

# Connect to SQLite database (or any other database of your choice)
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Create a table to store encrypted data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS encrypted_data1 (
        id INTEGER PRIMARY KEY,
        encrypted_text TEXT
    )
''')
conn.commit()

# Get user input
user_input = input("Enter data to encrypt and store: ")

# Encrypt the user input
encrypted_input = encrypt_data(user_input, encryption_key)

# Store the encrypted data in the database
cursor.execute('INSERT INTO encrypted_data1 (encrypted_text) VALUES (?)', (encrypted_input,))
conn.commit()

# Retrieve and decrypt data from the database
cursor.execute('SELECT encrypted_text FROM encrypted_data1 WHERE id = 1')
result = cursor.fetchone()

if result:
    decrypted_data = decrypt_data(result[0], encryption_key)
    print("Decrypted data:", decrypted_data)

# Close the database connection
conn.close()
