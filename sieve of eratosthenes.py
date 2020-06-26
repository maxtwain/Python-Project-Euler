import math, time
start = time.clock()

def prevPrimes(limit):
    """Generates a list of primes up to 'limit'"""
##    from numbers import Integral as types #'Integral' is a class of integers/long-numbers
##    if not isinstance(limit, types): raise TypeError("limit must be int, not " + str(type(limit)))
##    if limit < 2: raise ValueError("limit must greater than 2")
    # All odd values within limit = True
    primes_dict = {i : True for i in range(3, limit + 1, 2)}
    for i in primes_dict:
        # Checks only values in dict which are True
        if primes_dict[i]: #== True
            mult = 3
            #sets all multiples of i (up to limit) as False
            while (mult * i <= limit):
                primes_dict[mult * i] = False
                mult += 2
    primes_dict[2] = True
    return [i for i in primes_dict if primes_dict[i]] #== True


primeList = prevPrimes(2000000)
end = time.clock() - start
print("Time = {0:.2f} seconds".format(end))