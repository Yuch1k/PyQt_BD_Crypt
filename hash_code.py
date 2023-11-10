import hashlib


def sha_3(text, c_bytes):
    if c_bytes in ('224', '256', '384', '512'):
        h = hashlib.new(f'sha3_{c_bytes}')
        h.update(text.encode('UTF-8'))
        return h.hexdigest()


def sha_1(text, c_bytes):
    if c_bytes in ('224', '256', '384', '512'):
        h = hashlib.new(f'sha{c_bytes}')
        h.update(text.encode('UTF-8'))
        return h.hexdigest()


def md_5(text):
    h = hashlib.new('md5')
    h.update(text.encode('UTF-8'))
    return h.hexdigest()


def custom_hash(data):
    hash_sum = 0
    for char in data:
        hash_sum += ((abs((hash_sum // 23 + (ord(char) ** 3)) // len(data)) - 2345678) ** 2) % 10000002
    hash_x = hex(hash_sum)
    return hash_x
