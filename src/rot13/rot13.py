from file_utils import *
from ascii_utils import *

def Encrypt(plaintext, shift):

    temp_string = ""
    for c in plaintext:
        temp = (ord(c) + 13)
        if Is_Special_Character(c):
            temp_string += " "
        else:
            temp = ascii_range_reset(temp)
            c = chr(temp)
            temp_string += c

    return temp_string

def Decrypt(ciphertext, shift):

    temp_string = ""
    for c in ciphertext:
        temp = ord(c) - 13
        if Is_Special_Character(c):
            temp_string += " "
        else:
            temp = ascii_range_reset(temp)
            c = chr(temp)
            temp_string += c

    return temp_string
