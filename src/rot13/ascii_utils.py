# Utility functions to handle ascii characters

def Is_Special_Character(input_string):

    is_sc = False
    if (ord(input_string) < ord('A') or (ord(input_string) > ord('z'))):
        is_sc = True

    return is_sc

def ascii_range_reset(input_ascii):
    temp = 0
    if (input_ascii > 122):
        temp = input_ascii - 26
    elif (input_ascii < 97):
        temp = input_ascii + 26
    else:
        temp = input_ascii

    return temp
