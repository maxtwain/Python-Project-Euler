import math, time
start = time.clock()

def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

primeList = list(primes_sieve2(2000000))
end = time.clock() - start
print("Time = {0:.2f} seconds".format(end))