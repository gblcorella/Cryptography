from sha1 import *
from hash_comp import *

def publish_hash(m1):
    return Sha1Hash().update(m1.encode()).hexdigest()

def length_extension_attack(m2, pub_hash):
    return Sha1Hash(pub_hash, 128).update(m2.encode()).hexdigest()

def verify(m1, padding, m2):
    message = m1.encode() + padding + m2.encode()
    print("verify:", Sha1Hash().update(message).hexdigest())

def main():

    hash_comp()
    return
    m1 = "1mM6DRJMkWXgKY4Me3BRRtKf1wZq5Gm5ywmZofCLT3ngFMUYquLfmhJfLZVniwLR"

    m2 = "IyKnG5hp8A0gYbPCQgW3bg3dMinA2nm26nPObA82q85DX8ihArlEqxAzZ5FLuhB5"

    pub_hash = publish_hash(m1)
    padding = b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00'
    attack_hash = length_extension_attack(m2, pub_hash)

    print("attack:", attack_hash)
    print()
    verify(m1, padding, m2)

main()