import math, time
start = time.clock()

from mymath02 import div_gen

def ami_sum(limit):
    tested = []
    amiSum = 0
    for i in range(2, limit):
        if i in tested:
            continue
        divisorSum = sum(div_gen(i)) - i
        if divisorSum < limit and i != divisorSum:
            tested.append(divisorSum)
            if i == sum(div_gen(divisorSum)) - divisorSum:
                amiSum += i + divisorSum
    return amiSum

print(ami_sum(10000))

end = time.clock() - start
print("Time = {0:.2f} seconds".format(end))

