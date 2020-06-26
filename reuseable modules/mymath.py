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

def list_divisors(num):
    ''' Creates a list of all divisors of num
    '''
    orig_num = num
    prime_list = list_to_number(int(num ** (1/2)) + 1)
    divisors = [1]
    for i in prime_list:
        num = orig_num
        while not num % i:
            divisors.append(i)
            num = int(num / i)
    print(divisors)
    for i in range(1, len(divisors) - 1):
            for j in range(i + 1, len(divisors)):
                if not orig_num % (i * j):
                    divisors.append(i * j)
    divisors.append(num)
    divisors = list(set(divisors))
    divisors.sort()
    return divisors

end = time.clock() - start
print("Time = {0:.2f} seconds".format(end))