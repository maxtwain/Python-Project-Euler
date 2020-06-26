import math

def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def primes(n = 1):
    while(True):
        if isprime(n): yield n
        n += 1

# must yeild until limit is reached, then it must return primeList
def pToList(limit):
    primeList = []
    for n in primes():
        if n > limit: break
        primeList.append(n)

    return primeList


print(pToList(100))