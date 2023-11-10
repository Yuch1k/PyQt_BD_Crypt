import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes


def aes_256_encrypted(data, password, file_name):
    data = data.encode('UTF-8')
    password = password.encode('UTF-8')

    salt = get_random_bytes(32)

    key = hashlib.scrypt(password, salt=salt, n=2**14, r=8, p=1, dklen=32)
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    file_out = open(file_name, "wb")
    [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
    file_out.close()
    return salt


def aes_256_decrypted(file_name, password, salt):
    password = password.encode('UTF-8')
    file_in = open(file_name, "rb")
    nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]
    key = hashlib.scrypt(password, salt=salt, n=2**14, r=8, p=1, dklen=32)
    cipher = AES.new(key, AES.MODE_GCM, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data.decode('UTF-8')

