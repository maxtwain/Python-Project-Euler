import math, time
start = time.clock()

from itertools import permutations

def millionth_perm():
    count = 0
    for perm in permutations(range(10)):
        count += 1
        if count == 1000000:
            return int("".join(str(element) for element in perm))

print(millionth_perm())




end = time.clock() - start
print("Time = {0:.2f} seconds".format(end))