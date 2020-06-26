import math, time
start = time.clock()

def nextPrime(primeList):
    checkNum = 3
    while True:
        for i in primeList:
            if not checkNum % i: # == False
                break
            if i > math.sqrt(checkNum):
                yield checkNum
                break
        checkNum += 2

def primeNumbers(limit):
    primeList = [2]
    for i in nextPrime(primeList):
        if i > limit:
            break
        primeList.append(i)
    return primeList

primeList = primeNumbers(200)
print(primeList)


end = time.clock() - start
print("Time = " + str(end) + " seconds")