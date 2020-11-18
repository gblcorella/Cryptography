# Imports

#import random
import hashlib
from Crypto.Cipher import AES
from Crypto import Random

# Gabriel Corella
# Applied Crypto

# Init Hash Value of 32 Bits
def hashVal(seed):
  x = hashlib.sha256(seed)
  return x.digest()[0:4]

# Padding function at the end if below char limit for Question 3

def padding_func(message):
  vary = 32 - (len(message) + 3)
  byteorder = 'big' 
  if(vary > 0): 
    padded_output = message + b'\x80' + (b'\x00'*(16-(len(message) + 3))) +len(message).to_bytes(2,byteorder)
  else:
    padded_output = message + len(message).to_bytes(32-len(message),byteorder)
  return padded_output

def byte_xor(byte_a1, byte_a2):
    return bytes([a ^ b for a, b in zip(byte_a1, byte_a2)])

# Use the Rho method to find collisions
# Question 1 [15 Points]
def rho_method():
  print('Question 1: Rho Method... \n')
  i = 0
  #initialize two empty arrays to append
  first_arr = []
  second_arr = []

  firstVal =  hashVal(b"Please work for the love of God") # Random.get_random_bytes(4)
  copyFirst = firstVal

  hashedVal1 = hashVal(firstVal)
  hashedVal2 = hashVal(hashVal(copyFirst))
 # print('Hashed Values: ' + str(hashedVal1))
 # print('Hashed Values: ' + str(hashedVal2))
 
  first_arr.append(firstVal)
  first_arr.append(hashedVal1)
  second_arr.append(copyFirst)
  second_arr.append(hashedVal2)
  
  while second_arr[i+1] != first_arr[i+1]:
    first_arr.append(hashVal(first_arr[i]))
    second_arr.append(hashVal(hashVal(second_arr[i])))
    i = i+1
  print('What is the size of the cirle? Ans:', i,'\n')
rho_method()

# Question 2[30 points total]
# Implement a merkle_Damgard hash H 
randBits = Random.get_random_bytes(16)
key = Random.get_random_bytes(16)


def merkle_Damgard(message,hVal):
  message = message.encode()
  comp = len(message)//16
  if(len(message)%16 > 0):
    comp +=1
  h = hVal

  #print("Compression function.. ",comp,'\n')
  for i in range(0,comp):
    #github
    if(len(message[i*16:(i+1)*16]) == 16):
      encryptedtxt = AES.new(message[i*16:(i+1)*16],AES.MODE_ECB)
    else:
      m = padding_func(message[i*16:(i+1)*16]) 
      encryptedtxt = AES.new(m,AES.MODE_ECB)
      #Use xor function and return final
    finalTxt = byte_xor(h,encryptedtxt.encrypt(h))
  return finalTxt

x = merkle_Damgard("Testing...",randBits)
print("Testing Value: ", x,"\n Testing Length: ",len(x))

# Implement a secret prefix MAC based on 'H'
# concatanate the key and message and encode it. Part B

def secret_prefixMAC(message,k,h):
  return merkle_Damgard(k+message.encode(),h)

#forger for the 
def forger(m1,m2,h):
  key = Random.get_random_bytes(4)
  return secret_prefixMAC(m2.encode()+m1,key,h)

def extend_forger(m1,m2,h):
  return merkle_Damgard(m2.encode() + m1,h)

