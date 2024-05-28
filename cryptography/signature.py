import random
from math import gcd
import hashlib as hash


def coprime(a, b):
    return gcd(a, b) == 1


def generate_prime(lower_bound, upper_bound):
    #python programm which returns a list of primes between the two boundaries.
    primes = []
    for num in range(lower_bound, upper_bound + 1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)
    return primes

def find_coprime_to(coprime1):
    work_done = False
    while work_done is False:
        coprime2 = random.randint(2, coprime1 - 1)
        if coprime(coprime1, coprime2):
            work_done = True
    return coprime2

def Basic_RSA_keys(prime1, prime2):
    n = prime1 * prime2
    phi_n = (prime1 - 1) * (prime2 - 1)
    e = find_coprime_to(phi_n)

    public_signature_key = (e, n)

    private_signature_key = phi_n - (e ** (-1) % phi_n)

    return private_signature_key, public_signature_key

def Basic_RSA_sign(private_signature_key, message_encrypted, n):
    blake2b = int(hash.blake2b(bytes('test', 'utf-8'), digest_size=4).hexdigest() , 16)
    #sha256 = int(hash.sha256(bytes(message_encrypted, 'utf-8')).hexdigest(), 16)

    return ((blake2b ** private_signature_key) % n)

def Basic_RSA_verify(message_encrypted, signature, public_signature_key):
    blake2b = int(hash.blake2b(bytes('test', 'utf-8'), digest_size=4).hexdigest(), 16)
    #sha256 = int(hash.sha256(bytes(message_encrypted, 'utf-8')).hexdigest(), 16)

    check_1 = blake2b % public_signature_key[1]
    check_2 = (signature ** public_signature_key[0]) % public_signature_key[1]

    verified = False

    if check_1 == check_2:
        verified = True
    else:
        print(check_1, check_2, signature, public_signature_key[0], public_signature_key[1])
    return verified

keys = Basic_RSA_keys(3, 7)

sign = Basic_RSA_sign(keys[0], 'Lets suppose this is already encrypted', keys[1][1])

print(Basic_RSA_verify('Lets suppose this is already encrypted', sign, keys[1]))
