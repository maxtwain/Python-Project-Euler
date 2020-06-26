import time
start = time.clock()

def divisor_sum(factorThis):
    '''
    The sum of all proper divisors are returned.
    '''
    divisorSum = 1
    for divCheck in range(2, int(factorThis**0.5)+1):
        if factorThis % divCheck == 0:
            divisorSum += divCheck + factorThis / divCheck
    if factorThis**0.5 == int(factorThis**0.5):
        divisorSum -= factorThis**0.5
    return divisorSum

def abundant_sum(limit):
    abundantSum = 0
    abundantSet = set()
    # This loop checks for abundant numbers under limit.
    for check in range(1, limit):
        # If this is true, check is an abundant number.
        if divisor_sum(check) > check:
            # .add will add check to the list of abundants if it does not exist, else it will do nothing.
            abundantSet.add(check)
        if not any((check - abundant in abundantSet) for abundant in abundantSet):
            abundantSum += check
    return abundantSum

print(abundant_sum(20162))

end = time.clock() - start
print("Time = {0:.2f} seconds".format(end))