

def evenIndex(myWord):      
    tempWord = ''
    i = 0
    while i < len(myWord):
        if i % 2 == 0:
            tempWord += myWord[i]
        i += 1

    return tempWord