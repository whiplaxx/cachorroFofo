def startsWith(string1, string2):

    for i in range(0, len(string2)):
        if string1[i] != string2[i]:
            return False

    return True