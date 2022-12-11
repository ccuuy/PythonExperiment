from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding
import os

key = os.urandom(32)  # AES128->16, AES192->24, AES256->32
iv = os.urandom(16)


def encrypt_CBC(key, plaintext, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    # PKCS7填充,缺N个就补N个chr(N)
    padder = sym_padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext)
    padded_data += padder.finalize()
    ct = encryptor.update(padded_data) + encryptor.finalize()
    return ct


def decrypt_CBC(key, ciphertext, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = sym_padding.PKCS7(128).unpadder()
    pt = unpadder.update(padded_data)
    pt += unpadder.finalize()
    return pt


plaintxt = b"0123456789"*128

ciphertext = encrypt_CBC(key, plaintxt, iv)

text = decrypt_CBC(key, ciphertext, iv)

print(ciphertext)
print(text)
