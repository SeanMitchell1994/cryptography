from file_utils import *
from ascii_utils import *

def Encrypt(plaintext):

    temp_string = ""
    for c in plaintext:
        if Is_Special_Character(c):
            temp_string += c
        else:
            distance = ord('a') - ord(c)
            swap = ord('z') + distance
            temp_string += chr(swap)

    return temp_string

def Decrypt(ciphertext):

    temp_string = ""
    for c in ciphertext:
        if Is_Special_Character(c):
            temp_string += c
        else:
            distance = ord('z') - ord(c)
            swap = ord('a') + distance
            temp_string += chr(swap)

    return temp_string
