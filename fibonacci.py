import math, time
start = time.clock()

import itertools

def fib():
    fibList = [1, 1]
    count = 2
    while len(str(fibList[1])) < 1000:
        count += 1
        fibList.append(fibList[1] + fibList.pop(0))
    return count

print(fib())



end = time.clock() - start
print("Time = {0:.2f} seconds".format(end))