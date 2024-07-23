from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES

def deriveKey(text, salt, key_size=32):
    return PBKDF2(text, salt, dkLen=key_size, count=1000000)

def unpadData(data):
    padding_length = data[-1]
    return data[:-padding_length]

def decryptFile(input_path, output_path, key_text):
    with open(input_path, 'rb') as file:
        encrypted_data = file.read()
    salt = encrypted_data[:16]
    iv = encrypted_data[16:32]
    ciphertext = encrypted_data[32:]
    key = deriveKey(key_text, salt, 32)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = cipher.decrypt(ciphertext)
    data = unpadData(padded_data)
    with open(output_path, 'wb') as file:
        file.write(data)

# Example usage
encrypted_file_path = 'C:/Users/thetr/Documents/Python/SevenGatesOfHell/flowfree.gtfo'  # Replace with your encrypted file path
decrypted_file_path = 'C:/Users/thetr/Documents/Python/SevenGatesOfHell/flowfree_decrypted.mp4'  # Replace with your desired output file path
key_text = 'abcdefg'

decryptFile(encrypted_file_path, decrypted_file_path, key_text)
print(f"File decrypted and saved to {decrypted_file_path}")
