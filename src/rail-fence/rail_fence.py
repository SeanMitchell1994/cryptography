from file_utils import *
from ascii_utils import *

def Encrypt(plaintext, rails):

    temp_string = ""
    length = len(plaintext)
    string_arr = [""] * 3
    count = -1
    chk = False
    plaintext = "abcd"

    # This top loop is the length of the string to be encoded
    for c in plaintext:
        # This inner loop is the number of rails to be used
        for rail in range(rails):
            # Figure out if we are going up or down
            if (chk == False):
                if (count >= 2):
                    count = 1
                    chk = True
                else:
                    count += 1
            elif (chk == True):
                count -= 1
                if (count < 0):
                    count = 1
                    chk = False
            # This is broken
            # It appends to the array for every iteration, not just the correct indices
            print("rail: " + str(rail) + ", count: " + str(count) + " char: " + str(c))
            string_arr[count] += str(c)
            break


    for i in string_arr:
        temp_string += i
    print(string_arr)

    return temp_string

def Decrypt(ciphertext, rails):

    temp_string = ""
    return temp_string

def test2(n):
    for i in list(range(0, n + 1)) + list(range(n-1, -1, -1)):
        print(i)

def Next(count):
    # Returns next index of the rail

    chk = False
    #count = 0

    if (chk == False):
        count += 1
        if (count > 3):
            count = 3
            chk = True
    elif (chk == True):
        count -= 1
        if (count > 3):
            count = 3
            chk = False
    return count