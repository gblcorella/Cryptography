import hashlib
import string
import random
import time

def random_message():
    message = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(512)])
    return message

def time_hash_alg(hash_obj, n):
    m = random_message().encode()

    start = time.time()
    for i in range(n):
        hash_obj.update(m)
    end = time.time()
    return end - start

def hash_comp():
    n = 100000
    sha3_256 = hashlib.sha3_256()
    sha3_384 = hashlib.sha3_384()
    sha3_512 = hashlib.sha3_512()
    blake_2b = hashlib.blake2b()
    blake_2s = hashlib.blake2s()

    print("SHA3_256 time:", time_hash_alg(sha3_256, n))
    print("SHA3_384 time:", time_hash_alg(sha3_384, n))
    print("SHA3_512 time:", time_hash_alg(sha3_512, n))
    print("BLAKE2b time:", time_hash_alg(blake_2b, n))
    print("BLAKE2s time:", time_hash_alg(blake_2s, n))




