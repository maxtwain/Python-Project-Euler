

import math, time, operator
from userprimes import list_to_index, list_to_number
start = time.clock()

#this is an attempt to find a lower bound on a 500 divisor number
#unfinished function
def lowerBound():
    #Limit on prime factor list
    guessTarget = 500
    divisorList = [0, 1]
    #Limit on primes list
    upToNumber = 5000
    primeList = primeNumbers(upToNumber)
    for i in primeNumbers:
        expoI = i
        if len(divisorList) >= 500:
            break
        divisorList.append(i)
        while expoI < guessTarget / 2:
            expoI = expoI ** expoI

#this calculates 250!
def factorialExperiment():
    fact = 1
    for i in range(2, 250):
        fact *= i
    return fact

#this function generates a list of tri numbers
def triList(upto):
    triNums = [1]
    for i in range(2, upto):
        triNums.append(i + triNums[-1])
    print("TriNums loaded.  Time = " + str(time.clock() - start) + " seconds")
    return triNums



def init_fact():
    ''' Generates an initial dict of factors up to 500, and reduces
    them by previous factors.

    For example, 500 becomes 1 since 500 = 5 ** 3 * 2 ** 2,
    while 499 remains as it is since it is prime.
    4 however becomes 2 since only only one power of two precedes it.
    [ (2), (3), (4/2), (5), (6/(3*2)), (7), (8/(4*2), (9/(3)) ,(10/(5*2)),
    (11), (12/(4*3*2)), (13), (14/(7*2)), (15/(5*3)), (16/(8*2)), (17),
    (18/(9*2)), (19), (20/(10*2)), (21/(7*3)), (22/(11*2), (23), (24/(12*2)),
    (25/(5)), (26/(13*2)), (27/(7*3)), (28/(7*4)), (29), (30/(10*3)) ]
    '''
    fact = {factor + 1: reduced + 1 for factor, reduced in enumerate(range(500))}
    for factor, reduced in fact.items():
        if reduced < 4:
            continue
        for fCheck in range(int(reduced / 2) + 1, 1, -1):
            if not (reduced % fCheck):
                reduced = int(reduced / fCheck)
                fact[factor] = reduced
    return fact

def necessary_numbers(target, keyList):
    nec = []
    for target in keyList:
        for factor in range(2, int(target / 2) + 1):
            if not target % factor:
                target = target / factor
                if factor not in nec:
                    nec.append(factor)
                if target / factor not in nec:
                    nec.append(target / factor)
    return nec

def reduce_product():
    '''Here init_fact is received with factors 1 to 500.  The product of
    these numbers is enormous.  The goal of this function is to reduce
    this product to its lowest form by replacing factors that have not
    reduced to 1 with greater factors which do reduce to 1.
    Example: 499 may be replaced with 600, thus reducing the product of
    fact by the factor of 499 since 600 = 2 ** 3 * 3 * 5 ** 3.

    variables: greatestReduced

    This function should run until the point where the largest reduced can no
    longer be reduced.

    Note: This function is complete but it has failed its intention.
    '''
    fact = init_fact()
    keyList = list(fact.keys())
    valueList = list(fact.values())
    keyList.reverse()
    valueList.reverse()
    print(keyList, valueList)

    # Finds a higher maximum factor with a lower reduced.
    falseCount = 0
    currentFactor = max(keyList)
    while falseCount < 100:
        maxIndex = valueList.index(max(valueList))
        currentFactor = reduced = currentFactor + 1
        print("Checking {}".format(currentFactor))
        for i in valueList:
            if i != 1 and not reduced % i:
                reduced = int(reduced / i)
        if reduced < currentFactor:
            if reduced < max(valueList) and keyList[maxIndex] not in necessary_numbers(keyList[maxIndex], keyList):
                print("Replacing factors {} with {}.  Replacing reduced {} with {}.".format(keyList[maxIndex], currentFactor, valueList[maxIndex], reduced))
                keyList.pop(maxIndex)
                valueList.pop(maxIndex)
                keyList.append(currentFactor)
                valueList.append(reduced)
                falseCount -= 1
            else:
                falseCount += 1
    fact = {i: j for i, j in zip(keyList, valueList)}
    notOne = []
    prod = 1
    for i in valueList:
        if i != 1:
            notOne.append(i)
            prod*= i
    print("\n" + str(notOne) + "\n")
    print("Product = {}".format(prod))
    return fact

#check truth of tri number
def triTruth(query):
    checkRange = 10
    check = [0 for i in range(checkRange + 1)]
    check[0] = int(math.sqrt(query))
    for i in range(checkRange):
        check[i + 1] = int((check[i] - (check[i] * (check[i] + 1) - 2 * query)
        / (2 * check[i] + 1)))
    lastValue = int(check[-1] * (check[-1] + 1) / 2)
    if lastValue == query:
        print("Checking {}: True".format(query))
        print("The " + str(check[-1]) + "th triangle number is " + str(query))
        return True
    else:
##        print("\nCheck Values = " + str(check))
        print("\nChecking {}: False".format(query))
        print("The " + str(check[-1]) + "th triangle number is t = " + str(lastValue))
        print("The difference: FHF - t = " + str(query - lastValue))
        return False

def factors_over_500():
    '''Another failed attempt.
    '''
    numFact = 500
    lowNumber = 2 ** 249
    while numFact < 600:
        numFact += 1
        for a in range(42, 4, -1):
            for b in range(int(numFact / a), 1, -1):
                for c in range(int((numFact / a) / b), 0, -1):
                    for d in range(int(((numFact / a) / b) / c), 0, -1):
                        for e in range(2):
                            for f in range(2):
                                for g in range(2):
                                    for h in range(2):
                                        if numFact == (a + 1)*(b + 1)*(c + 1)*(d + 1)*(e + 1)*(f + 1)*(g + 1)*(h + 1) and e < d and f < e and g < f and h < g:
                                            currentNumber = (2 ** a) * (3 ** b) * (5 ** c) * (7 ** d) * (11 ** e) * (13 ** f) * (17 ** g) * (19 ** h)
                                            if currentNumber < lowNumber:
                                                lowNumber = currentNumber
    return lowNumber

def factors_over_500_v2():
    numFact = 500
    lowNumber = 2 ** 249
    basicPrimeList = [2, 3, 5, 7, 11, 13, 17, 19]
    answerList = []
    while numFact < 600:
        factorList = []
        reduced = numFact = numFact + 1
        if numFact == list_to_number(numFact + 1)[-1]:
            continue
        for i in list_to_number(int(numFact / 2) + 1):
            while not reduced % i:
                factorList.append(i)
                reduced = int(reduced / i)
            if reduced == 1:
                break
        currentProduct = 1
        factorList.reverse()
        for i, j in zip(factorList, basicPrimeList):
            currentProduct *= j ** (i-1)
        if currentProduct < lowNumber:
            lowNumber = currentProduct
        answerList.append(currentProduct)
        answerList.sort()
    return answerList

def reassemble(answerList):
    basicPrimeList = [2, 3, 5, 7, 11, 13, 17, 19]
    reassembledAnswers = []
    for newAnswer in answerList:
        for oldDivisor in basicPrimeList:
            for newDivisor in basicPrimeList:
                if not newAnswer % oldDivisor and oldDivisor != newDivisor:
                    reassembledAnswers.append(int(newAnswer * newDivisor / oldDivisor))
    return reassembledAnswers

def my_main():
    answerList = factors_over_500_v2()
    reassembledAnswers = reassemble(answerList)
    truthList = []
    for i in answerList:
        if triTruth(i):
            truthList.append(i)
    for i in reassembledAnswers:
        if triTruth(i):
            truthList.append(i)
    truthList.sort()
    return truthList

print(my_main())


##query = 199999990000001
##print(str(triTruth(query)))

##upto = 20
##triList = triList(upto)
##print(str(upto) + "th tri number = " + str(triList[-1]))
end = time.clock() - start
print("Program finished.  Time = " + str(end) + " seconds")