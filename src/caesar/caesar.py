from file_utils import *
from ascii_utils import *

def Encrypt(plaintext, shift):

    temp_string = ""
    for c in plaintext:
        if c.lower == "z":
            c = "a"
        temp = (ord(c) + shift)
        if Is_Special_Character(c):
            temp_string += c
        else:
            c = chr(temp)
            temp_string += c

    return temp_string

def Decrypt(ciphertext, shift):

    temp_string = ""
    for c in ciphertext:
        temp = ord(c) - shift
        if Is_Special_Character(c):
            temp_string += c
        else:
            c = chr(temp)
            temp_string += c

    return temp_string