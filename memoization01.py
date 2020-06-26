import math, time
start = time.clock()

def solution02():
    cache, maxPair = {1:1}, (0, 0)

    def check(num):
        if num not in cache:
            cache[num] = check(3 * num + 1 if num % 2 else int(num/2)) + 1
        return cache[num]

    for num in range(500000, 1000000):
        if check(num) > maxPair[1]:
            maxPair = (num, check(num))
    return maxPair

def solution03():
    priorChains = [0,1]
    for actual in range(2,1000000):
        n = actual
        lenChain = 1
        while n != 1:
            if n & 1:     # if odd
                n = 3*n + 1
                lenChain+=1
            else:
                n = int(n / 2)
                if n < actual:
                    lenChain+=priorChains[n]
                    break
        priorChains.append(lenChain)
    return priorChains.index(max(priorChains))

print(solution03())

end = time.clock() - start
print("Time = {0:.2f} seconds".format(end))