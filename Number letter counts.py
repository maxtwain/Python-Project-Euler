import math, time
start = time.clock()

##def buildRefTest():
##    wordRefKeys = []
##    wordRefVals = []
##    for i in wordRef.keys():
##        wordRefKeys.append(i)
##    for i in wordRef.values():
##        wordRefVals.append(i)
##    for i in range(len(wordRefKeys)):
##        print(wordRefKeys[i], wordRefVals[i])
##    print("\n")

def buildRef():
    wordRef = {0: 0}
    twentyRefList = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8, 6]
    tensRefList = [6, 5, 5, 5, 7, 6, 6]
    for i in range(1, 21):
        wordRef[i] = twentyRefList[i]
    for i in range(3, 10):
        wordRef[i*10] = tensRefList[i - 3]
    for i in range(1, 10):
        wordRef[i * 100] = twentyRefList[i] + 7
    wordRef[1000] = 11
    return wordRef

def wordSum(num):
    wordSum = 0
    wordRef = buildRef()
    tens, hundreds = 0, 0
    for i in range(1, num + 1):
        if i in wordRef:
            wordSum += wordRef[i]
        elif i < 100:
            wordSum += wordRef[int(i / 10) * 10] + wordRef[i % 10]
        else:
            wordSum += wordRef[int(i / 100) * 100] + 3
            if i % 100 < 20:
                wordSum += wordRef[i % 100]
            else:
                wordSum += wordRef[int((i % 100) / 10) * 10] + wordRef[i % 10]
    return wordSum

print(wordSum(1000))

end = time.clock() - start
print("Time = {0:.2f} seconds".format(end))