import itertools

def prime_gen():
     '''
    This function generates prime numbers using the sieve of erat.  Instead of
    storing a list of numbers to elminate, this function stores the next multiple
    of a prime to eliminate.  This means that when a prime is found, its next
    multiple - or composite - is saved into a list of non-primes.  When that
    non-prime number is reached in the list, the composite is increased by
    its prime factor over and over again until the function is no longer called.
    This list begins with the square of a prime, then is increased with the
    cube of the prime, then with the fourth exponent, and so on forever.
    '''
     comp = {} # map each composite integer to its first-found prime factor
     for counter in itertools.count(2): # counter gets 2, 3, 4, 5, ... ad infinitum
        getValue = comp.pop(counter, None)
        if getValue is None:
            # counter not a key in comp, so counter is prime, therefore, yield it

            yield counter
            # mark counter squared, as not-prime (with counter as first-found prime factor)
            # counter ** 2 represents the end of our range of composites.
            # counter is its smallest prime factor, and the amount by which it
            # must be increased in order to find the next composite in its order
            # if / when we are required to move beyond counter ** 2.
            comp[counter ** 2] = counter
        else:
            # let fact <- smallest (N* getValue)+counter which wasn't yet known to be composite
            # we just learned fact is composite, with getValue first-found prime factor,
            # since getValue is the first-found prime factor of counter -- find and mark it
            fact = getValue + counter
            while fact in comp:
                fact += getValue
            comp[fact] = getValue
