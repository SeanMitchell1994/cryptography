from file_utils import *
from ascii_utils import *

def Encrypt(plaintext, rails):

    temp_string = ""
    length = len(plaintext)
    string_arr = [""] * 3
    count = 0
    chk = False

    #for i in range(rails):
    #    for j in range(length):
    #        print("* ",end="")
    #    print("")

    for c in range(6):
        for rail in range(rails):
            if rail == count:
                #print(Next(rail))
                #print("1 ")
                print(count)
                string_arr[count] += str(count)
            #else:
                #print("")
        #print(" ")

        if (chk == False):

            if (count > 2):
                count = 1
                chk = True
            else:
                count += 1
        elif (chk == True):
            count -= 1
            if (count < 0):
                count = 0
                chk = False

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