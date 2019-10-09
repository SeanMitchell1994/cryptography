from file_utils import *

def Encrypt(plaintext):

    temp_string = ""
    for c in plaintext:
        distance = ord('a') - ord(c)
        swap = ord('z') + distance
        temp_string += chr(swap)

    return temp_string

def Decrypt(ciphertext):

    temp_string = ""
    for c in ciphertext:
        temp = ord(c) - 13
        if temp < ord('a'):
            temp_string += " "
        else:
            c = chr(temp)
            temp_string += c

    return temp_string
