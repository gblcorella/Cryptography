# ECDH w/ NIST Curves
# pip install tinyec
import tinyec.ec as ec
import tinyec.registry as reg
import secrets

# ECDH w/ Curve25519
# pip install donna25519
from donna25519 import PrivateKey

# ECDSA w/ NIST Curves or Brainpool
# pip install fastecdsa
from fastecdsa import keys, curve, ecdsa
from hashlib import sha256

# Elliptic Curve IES
# pip install eciespy
from ecies.utils import generate_key
from ecies import encrypt, decrypt

import time
import os 

def ecdh(curve_name):

  # generate keys
  begin = time.time()
  curve = reg.get_curve(curve_name)
  alice_sk = secrets.randbelow(curve.field.n)
  alice_pk = alice_sk * curve.g

  bob_sk = secrets.randbelow(curve.field.n)
  bob_pk = bob_sk * curve.g

  # key exchange
  alice_ss = alice_sk * bob_pk
  bob_ss = bob_sk * alice_pk
  end = time.time() - begin

  # check if shared secrets are equal
  if (alice_ss != bob_ss):
    print("Something went wrong!")
    return 0
  
  return end

def digital_signature(curve, message):
    sk, pk = keys.gen_keypair(curve)

    # hash message and sign
    r,s = ecdsa.sign(message, sk, hashfunc=sha256)

    # verify signature
    valid = ecdsa.verify((r,s), message, pk, hashfunc=sha256)

    return valid

def ies(ptxt):
    sk = generate_key()
    sk_bytes = sk.secret
    pk_bytes = sk.public_key.format(True) 
    ctxt = encrypt(pk_bytes, ptxt.encode())
    print("Ctxt:", ctxt)
    return decrypt(sk_bytes, ctxt)


# NIST Curves
print('='*30)
print("NIST Curves ECDH")
p192_time = ecdh('secP192r1')
print("P192 time:", p192_time, "s")

p224_time = ecdh('secP224r1')
print("P224 time:", p224_time, "s")

p256_time = ecdh('secP256r1')
print("P256 time:", p256_time, "s")

p384_time = ecdh('secP384r1')
print("P384 time:", p384_time, "s")

p521_time = ecdh('secP521r1')
print("P521 time:", p521_time, "s")
print('='*30)
print()

# Curve 25519 ECDH
print('='*30)
print("Curve 25519 ECDH\n")
start = time.time()
sk_alice = PrivateKey(os.urandom(32))
pk_alice = sk_alice.get_public()
sk_bob = PrivateKey(os.urandom(32))
pk_bob = sk_bob.get_public()
alice_ss = sk_alice.do_exchange(pk_bob)
bob_ss = sk_bob.do_exchange(pk_alice)
elapsed_time = time.time() - start
print("Alice Shared Secret:", alice_ss)
print("Bob Shared Secret:", bob_ss)
print("Shared Secrets Equal:", bob_ss == alice_ss)
print("Time:", elapsed_time)
print('='*30)
print()

# ECDSA w/ NIST P512
print('='*30)
print("ECDSA P256 with SHA256\n")
start = time.time()
print("Verify:", digital_signature(curve.P256, "plaintext"))
print("Time to sign and verify:", time.time() - start) 
print('='*30)
print()

# IES w/ NIST P256
print('='*30)
print("IES with P256")
start = time.time()
ptxt = "appliedcrypto"
print("Plaintext:", ptxt.encode())
result = ies(ptxt)
print("Recovered Plaintext:", result)
print('='*30)