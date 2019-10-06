# Utility functions to handle files

def Read_File(filename):
    f = open(filename,"r")
    lines = []
    for line in f:
        lines.append(line)
        
    lines = [x.strip() for x in lines]

    return lines

def Create_File(filename):
    f = open(filename, "w+")
    return 0

def Write_to_File(filename, text):
    f = open(filename, "a+")
    f.write(text)
    f.close()
    return 0