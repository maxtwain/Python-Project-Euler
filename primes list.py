

# create list [2, 3, 5, 7, 11, 13]
# initialize primeIndex at 6
# begin while loop, terminate when primeIndex == 1001
# initialize check variable at list[-1] + 2
# begin for loop with range(len(list))
# compare check variable with all values in list
# if not divisable, append check to list
# if divisable, do nothing.
# after termination of while loop, return list[primeIndex]

import math, time
start = time.clock()

def primeNumbers(limit):
    primeList = [2]
    checkNum = 3
    while checkNum <= limit:
        for i in primeList:
            if checkNum % i == 0:
                break
            if i > math.sqrt(checkNum):
                primeList.append(checkNum)
                break
        checkNum += 2
    return primeList

def prevPrimes(n):
    """Generates a list of primes up to 'n'"""
    from numbers import Integral as types #'Integral' is a class of integers/long-numbers
    if not isinstance(n, types): raise TypeError("n must be int, not " + str(type(n)))
    if n < 2: raise ValueError("n must greater than 2")
    primes_dict = {i : True for i in range(2, n + 1)} # initializes the dictionary
    for i in primes_dict:
        if primes_dict[i]: #avoids going through multiples of numbers already declared False
            num = 2
            while (num * i <= n): #sets all multiples of i (up to n) as False
                primes_dict[num*i] = False
                num += 1
    return [num for num in primes_dict if primes_dict[num]]


primeList = primeNumbers(2000000)
print(len(primeList))
end = time.clock() - start
print("Time = " + str(end) + " seconds")