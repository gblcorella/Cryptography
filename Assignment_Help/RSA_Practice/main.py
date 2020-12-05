import time
from random import randint
from Crypto.PublicKey import RSA
from Crypto.Signature import pss
from Crypto.Hash import SHA256

tabs = 24
alice_pk = ''
bob_pk = ''


def sign(rsa_sk, message):
    h = SHA256.new(message.to_bytes(4, byteorder='little'))
    signature = pss.new(rsa_sk).sign(h)
    return signature


def verify(rsa_pk, h, signature):
    verif = pss.new(rsa_pk)
    try:
        verif.verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False


def keygen(key_size, owner):
    sk = RSA.generate(key_size)
    f = open('private-' + owner + '.pem', 'wb')
    f.write(sk.export_key('PEM'))  # realistically, you need a passcode here for security
    f.close()

    pk = sk.publickey().export_key()
    f = open('public-' + owner + '.pem', 'wb')
    f.write(pk)
    f.close()


def alice(p, g, alice_sk, bob_sk):
    print()
    print("Alice:")
    a = randint(1, p - 1)
    print("\tprivate a:", a)
    A = pow(g, a, p)
    print("\tpublic A (g^a mod p):", A)
    sig_A = sign(alice_sk, A)
    print("Alice sends Bob: A and signature...")
    print()
    time.sleep(2)
    B, sig_B = bob(p, g, A, sig_A, bob_sk)
    hash_B = SHA256.new(B.to_bytes(4, byteorder='little'))
    isVerif = verify(bob_pk, hash_B, sig_B)
    shared_key = pow(B, a, p)
    print("Alice:")
    print("verify signature of B:", isVerif)
    print("Shared key is (B^a mod p):", shared_key)
    return


def bob(p, g, A, sig_A, bob_sk):
    print('\t' * tabs + "Bob:")
    b = randint(1, p - 1)
    print('\t' * tabs + "\tprivate b:", b)
    B = pow(g, b, p)
    print('\t' * tabs + "\tpublic B (g^b mod p):", B)
    hash_A = SHA256.new(A.to_bytes(4, byteorder='little'))
    isVerif = verify(alice_pk, hash_A, sig_A)
    print('\t' * tabs + "\tverify signature of A:", isVerif)
    shared_key = pow(A, b, p)
    print('\t' * tabs + "\tShared key is (A^b mod p):", shared_key)
    sig_B = sign(bob_sk, B)
    print('\t' * tabs + "Bob sends Alice: B and signature...")
    time.sleep(2)
    print()
    return B, sig_B


def alice_mqv(p, g):
    print()
    print("Alice:")
    a = randint(1, p - 1)
    x = randint(1, p - 1)
    print("\tprivate a:", a)
    print("\tprivate x:", x)
    A = pow(g, a, p)
    X = pow(g, x, p)
    print("\tsession A (g^a mod p):", A)
    print("\tpublic X (g^x mod p):", X)
    print("Alice sends A to Bob. Bob already knows Alice's public X...")
    print()
    time.sleep(2)
    B, Y = bob_mqv(p, g, A, X)
    Y_B = pow(Y, B, p)
    temp = (B * Y_B) % p
    a_xA = a + x * A
    shared_key = pow(temp, a_xA, p)
    print("Alice:")
    print("Shared key is (B * Y^B)^(a+xA) mod p:", shared_key)
    return


def bob_mqv(p, g, A, X):
    print('\t' * tabs + "Bob:")
    b = randint(1, p - 1)
    y = randint(1, p - 1)
    print('\t' * tabs + "\tprivate b:", b)
    print('\t' * tabs + "\tprivate y:", y)
    B = pow(g, b, p)
    Y = pow(g, y, p)
    print('\t' * tabs + "\tsession B (g^b mod p):", B)
    print('\t' * tabs + "\tpublic Y (g^y mod p):", Y)
    X_A = pow(X, A, p)
    temp = (A * X_A) % p
    b_yB = b + y * B
    shared_key = pow(temp, b_yB, p)
    print('\t' * tabs + "\tShared key is (A * X^A)^(b+yB) mod p:", shared_key)
    print('\t' * tabs + "Bob sends B to Alice. Alice already knows Bob's public Y...")
    time.sleep(2)
    print()
    return B, Y


def main():
    global bob_pk, alice_pk
    print('=' * 128)
    print("Authenticated Diffie-Hellman between two parties")
    print()
    p = 134471  # shared prime
    # p = 17435187646376611621 # 4096 bit prime
    print("p:", p)
    g = randint(1, 1000)  # shared base
    print("g:", g)
    print()
    keygen(2048, "alice")
    f = open('private-alice.pem', 'r')
    alice_sk = RSA.import_key(f.read())
    f.close()
    f = open('public-alice.pem', 'r')
    alice_pk = RSA.import_key(f.read())
    f.close()
    keygen(2048, "bob")
    f = open('private-bob.pem', 'r')
    bob_sk = RSA.import_key(f.read())
    f.close()
    f = open('public-bob.pem', 'r')
    bob_pk = RSA.import_key(f.read())
    f.close()
    alice(p, g, alice_sk, bob_sk)
    print('=' * 128)
    print()
    print('=' * 128)
    print("MQV Protocol")
    print()
    p = 503
    g = 2
    print("p:", p)
    print("g:", g)
    alice_mqv(p, g)
    print('=' * 128)
    print()
    print('=' * 128)
    print("D-H Shared Secret Bias")
    print()
    print("p:", 23)
    print("g:", 5)
    probs = [0, 0, 0, 0, 0]
    for i in range(22):
        num = '{:05b}'.format(5 ** i % 23)
        print(num)
        for j in range(len(num)):
            if int(num[j]) == 1:
                probs[j] += 1

    print()
    for i in range(len(probs)):
        print("probability of 1 at bit " + str(i) + ":", probs[i] / 23)

    print()


main()