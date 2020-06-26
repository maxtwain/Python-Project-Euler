import math, time
start = time.clock()

def primes_sieve2(limit):
    a = [True] * int((limit + 1) / 2)            # Initialize the primality list
    yield 2

    for (i, isprime) in enumerate(a):
        if isprime and i:
            adj = i * 2 + 1
            yield adj
            for n in range(adj ** 2, limit, adj * 2):   # Mark factors non-prime
                a[int((n - 1) / 2)] = False

primeList = list(primes_sieve2(2000000))
end = time.clock() - start
print("Time = {0:.2f} seconds".format(end))