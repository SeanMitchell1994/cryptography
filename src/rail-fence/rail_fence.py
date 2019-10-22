from file_utils import *
from ascii_utils import *

def Encrypt(plaintext, rails):

    temp_string = ""
    string_arr = [""] * rails
    count = -1
    chk = False

    plaintext = plaintext.replace(" ", "")

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
    string_arr = [""] * rails
    count = -1
    chk = False
    #i = 0
    #j = 0

    #for i in range(0,len(ciphertext),rails):
    #    print(ciphertext[(i - rails):i])

    # Decode algorithm is:
    # assume c is starting character
    # move forward key + 1 characters
    # next character is next decoded character
    # go back to c and increment
    #
    # Seems to work only for key of 2
    for i in range(len(ciphertext) // rails):       # Floor division by # of rails
        temp_string += ciphertext[i]
        if ((i + rails + 1) < len(ciphertext)):
            #print(ciphertext[i + rails + 1])
            temp_string += ciphertext[i + rails + 1]
        else:
            break

    return temp_string

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