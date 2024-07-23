from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import os

def derive_key(text, salt, key_size=32):
    # Derive a key using PBKDF2
    return PBKDF2(text, salt, dkLen=key_size, count=1000000)

def pad_data(data):
    # Pad data to be a multiple of 16 bytes
    padding_length = 16 - (len(data) % 16)
    return data + (padding_length * chr(padding_length)).encode()

def encrypt_file(input_path, output_path, key_text):
    # Read the file content
    with open(input_path, 'rb') as file:
        file_data = file.read()

    # Derive a key from the text key
    salt = get_random_bytes(16)  # Generate a random salt
    key = derive_key(key_text, salt, 32)  # Derive a 32-byte key for AES-256

    # Pad the file data
    padded_data = pad_data(file_data)

    # Generate a random IV
    iv = get_random_bytes(16)

    # Create AES cipher in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Encrypt the data
    ciphertext = cipher.encrypt(padded_data)

    # Concatenate salt, IV, and ciphertext
    encrypted_data = salt + iv + ciphertext

    # Write the encrypted data to the output file
    with open(output_path, 'wb') as file:
        file.write(encrypted_data)

# Example usage
input_file_path = 'D:/Videos/flowfree.mp4'  # Replace with your input file path
output_file_path = 'C:/Users/thetr/Documents/Python/SevenGatesOfHell/flowfree.gtfo'  # Replace with your desired output file path
key_text = 'abcdefg'

encrypt_file(input_file_path, output_file_path, key_text)
print(f"File encrypted and saved to {output_file_path}")
