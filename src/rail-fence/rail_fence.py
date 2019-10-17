from file_utils import *
from ascii_utils import *

def Encrypt(plaintext, rails):

    temp_string = ""
    string_arr = [""] * rails
    count = -1
    chk = False

    # This loop is index by the string to be encoded
    for c in plaintext:
        # Figure out if we are going up or down
        if (chk == False):
            # going down
            if (count >= (rails - 1)):
                count = (rails - 2)
                chk = True
            else:
                count += 1
        elif (chk == True):
            # going up
            count -= 1
            if (count < 0):
                count = 1
                chk = False

        #print("count: " + str(count) + " char: " + str(c))
        string_arr[count] += str(c)

    # concatenate resulting string
    for i in string_arr:
        temp_string += i
    #print(string_arr)

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