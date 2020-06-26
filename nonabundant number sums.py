import time
start = time.clock()

import itertools
import mymath02

def factor_sum(factorThis):
    '''
    The sum of all proper divisors are returned.
    '''
    factorSum, factorMax = 1, int(factorThis**0.5)
    for divisor in range(2, factorMax+1):
        if factorThis % divisor == 0:
            factorSum += (factorThis // divisor)
            if divisor != (factorThis // divisor):
                factorSum += divisor
    return factorSum

def abundant_gen():
    for i in itertools.count(12):
        if i < factor_sum(i):
            yield i

def root_abundant(limit):
    '''
    Most abundant numbers are multiples of root abundants, such as 24 from 12,
    and 60 from 20.  This function returns a list of only these roots.
    This is unfinished.
    '''
    rootList = [12]
    for check in range(limit):
        for root in rootList:
            if check % root == 0:
                break
            elif check < factor_sum(check):
                rootList.append(check)
                if len(rootList) % 100 == 0:
                    print(len(rootList))
                break
    return rootList

def root_gen():
    '''
    Most abundant numbers are multiples of root abundants, such as 24 from 12,
    and 60 from 20.  This sieve function yields these roots.
    '''
    rootDict = {}
    for abundant in abundant_gen():
        getValue = rootDict.pop(abundant, None)
        if getValue is None:
            yield abundant
            rootDict[abundant * 2] = abundant
        else:
            abundant += getValue
            while abundant in rootDict:
                abundant += getValue
            rootDict[abundant] = getValue

def abundant_list(limit):
    abunNums = []
    for i in abundant_gen():
        if i > limit: break
        abunNums.append(i)
    return abunNums


def sum_check(limit):
    '''
    This is broken.
    '''
    nonabundantSumed = []
    for asumCheck in range(limit):
        for abundant1 in abundant_gen():
            if asumCheck < abundant1:
                nonabundantSumed.append(asumCheck)
                break
            for abundant2 in abundant_gen():
                if asumCheck <= abundant1 + abundant2:
                    break
    return nonabundantSumed

def sum_list(limit):
    '''
    This is unfinished.
    '''
    sumList = []
    for abundant1 in abundant_gen():
        if abundant1 > limit:
            return sorted(sumList)
        for abundant2 in abundant_gen():
            abundantSum = abundant1 + abundant2
            if abundantSum > limit:
                break
            elif abundantSum not in sumList:
                sumList.append(abundantSum)

def nonabundant_sums(limit):
    '''
    The full abundant generator function as well as the abundant root
    function are iterated over to return nonabundant sums.
    This is unfinished.
    '''
    nonsumList = []
    for check in range(limit):
        if not sum_abundance(check):
            nonsumList.append(check)
    return nonsumList

def sum_abundance(check):
    '''
    A number is checked to see if it is the sum of two abundant numbers.
    If it is, True is returned.  If it is not, False is returned.
    '''
    for abundant in abundant_gen():
        if abundant * 2 > check:
            return False
        for abundantRoot in root_gen():
            # check is an abundant sum; break. needs to continue check loop.
            if (check - abundant) % abundantRoot == 0:
                return True
            elif (check - abundant) / abundantRoot < 1:
                break

def compare_lists(list1, list2):
    for i in list1:
        if i in list2:
            return False
    return True

print(sum(nonabundant_sums(28124)))



end = time.clock() - start
print("Time = {0:.2f} seconds".format(end))