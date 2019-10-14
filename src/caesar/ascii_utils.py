# Utility functions to handle ascii characters

def Is_Special_Character(input_string):

    is_sc = False
    if (ord(input_string) < ord('A') or (ord(input_string) > ord('z'))):
        is_sc = True

    return is_sc
