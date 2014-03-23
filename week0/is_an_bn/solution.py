def is_an_bn(word):
    countera = 0
    counterb = 0
    if word == "":
        return True
    elif word[0] != 'a':
        return False
    else:
        for i in range(0,len(word)):
            if word[i] == 'a' :
                if i != 0 and word[i - 1] != 'a':
                    return False
                else:
                    countera += 1
            elif (word[i] == 'b' and word[i - 1] == 'a') or (word[i] == 'b' and word[i - 1] == 'b'):
                counterb += 1
            else:
                return False
        return counterb == countera
