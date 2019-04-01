import time
import requests
from collections import Counter


def get_text():
    file = requests.get('https://projecteuler.net/project/resources/p059_cipher.txt').text
    return list(map(int, file.strip().split(',')))


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('{} ran in : {} sec'.format(func.__name__, end-start))
        return result
    return wrapper


@timer
def decryption():
    message = get_text()

    key = [Counter(message[i::3]).most_common(1)[0][0] ^ 32 for i in range(3)]

    print("Encryption key :", ''.join(map(chr, key)))

    key = key*(len(message)//3)

    decoded_msg = [x ^ y for x, y in zip(message, key)]
    decoded_msg = "".join(chr(x) for x in decoded_msg)

    print("Decoded message :", decoded_msg)

    print("Sum of ASCII values in decoded message :", sum(x ^ y for x, y in zip(message, key)))


decryption()
