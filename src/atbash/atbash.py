from file_utils import *

def Encrypt(plaintext, shift):

    temp_string = ""
    for c in plaintext:
        if c.lower == "z":
            c = "a"
        temp = (ord(c) + 13)
        if temp < ord('a'):
            temp_string += " "
        else:
            c = chr(temp)
            temp_string += c

    return temp_string

def Decrypt(ciphertext, shift):

    temp_string = ""
    for c in ciphertext:
        temp = ord(c) - 13
        if temp < ord('a'):
            temp_string += " "
        else:
            c = chr(temp)
            temp_string += c

    return temp_string