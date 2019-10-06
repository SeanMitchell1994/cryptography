from file_utils import *

def Encrypt(plaintext, shift):

    temp_string = ""
    for c in plaintext:
        temp = (ord(c) + shift)
        c = chr(temp)
        temp_string += c

    return temp_string

def Decrypt(ciphertext, shift):

    temp_string = ""
    for c in ciphertext:
        temp = ord(c) - shift
        c = chr(temp)
        temp_string += c

    return temp_string