import math, time
start = time.clock()

def factor_sum(factorThis):
    factorSum, factorMax = 1, int(factorThis**0.5)
    for divisor in range(2, factorMax+1):
        if factorThis % divisor == 0:
            factorSum += (factorThis // divisor)
            if divisor != (factorThis // divisor):
                factorSum += divisor
    return factorSum

def num_sums():
    numSums = {}
    for findSum in range(1,10000):	#populates dictionary of numbers and their factor sums
        numSums[findSum] = factor_sum(findSum)
    totalSum = 0
    for key in numSums:
        if numSums[key] in numSums and numSums[numSums[key]] == key and key != numSums[key]:
            totalSum += key

print (factor_sum(25))

end = time.clock() - start
print("Time = {0:.2f} seconds".format(end))