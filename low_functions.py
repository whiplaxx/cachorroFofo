def startsWith(string1, string2, ignoreSpaces = 1):

    if ignoreSpaces == 1:
        b = 0
        while string1[b] == ' ' or string1[b] == '\n':
            b += 1
        
    for i in range(0, len(string2)):
        if string1[i+b] != string2[i]:
            return False

    return True

if __name__ == "__main__":
    pass