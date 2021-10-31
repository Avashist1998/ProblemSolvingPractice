def UniqueString(word):
    boolSet = [False]*128
    for charters in word:
        index = ord(charters)
        if boolSet[index]:
            return True
        boolSet[index] = True
    return False

if __name__ == "__main__":
    str = "works"
    str2 = "does not work"
    print("This result of the string 1 : {}".format(UniqueString(str)))
    print("This result of the string 2 : {}".format(UniqueString(str2)))