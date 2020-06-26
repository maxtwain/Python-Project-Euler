import math, time
start = time.clock()

# This constant is more or less an overestimate for the range in which
# n primes exist.  Generally 100 primes exist well within 100 * CONST numbers.
CONST = 20

def iter_primes(limit):
    ''' This function yields primes using the
    Sieve of Eratosthenes.

    '''
    opRange = [True] * limit
    opRange[0] = opRange[1] = False

    for ind, primeCheck in enumerate(opRange):
        if primeCheck:
            yield ind
            for i in range(ind*ind, limit, ind):
                opRange[i] = False

def list_to_prime(termin):
    ''' Returns a list of primes up to the nth
    prime.
    '''
    primeList = []
    for i in iter_primes(termin * CONST):
        primeList.append(i)
        if len(primeList) >= termin:
            break
    return primeList

def list_to_number(termin):
    ''' Returns a list of primes up to the
    number termin.
    '''
    return list(iter_primes(termin))

list_to_prime(1000000)

end = time.clock() - start
print("Time = {0:.2f} seconds".format(end))