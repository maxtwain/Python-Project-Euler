import math, time
start = time.clock()


def name_score():
    with open('F:/Programming/python/project euler/names.txt') as nameFile:
        nameList = sorted(name.strip('"') for name in nameFile.read().split(','))
    scoreSum = 0
    for index in range(len(nameList)):
        alphaScore = 0
        for letter in nameList[index]:
            alphaScore += ord(letter) - 64
        scoreSum += (index + 1) * alphaScore
    return scoreSum

print(name_score())



end = time.clock() - start
print("Time = {0:.2f} seconds".format(end))