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


cache = {}
def sumFun(squares, size):
    if not squares - 2:
        return size
    else:
        nextResult = sumFun(squares - 1, size)
        cache[squares] = nextResult * int((nextResult + 1) / 2)
        if not squares - size:
            cache[squares] += 1
    return cache[squares]

def params():
    size = 3
    for i in range(2, size):
        print(i, sumFun(i, size))

def pascal(size):
    topAns = 1
    botAns = 1
    for i in range(1, 2 * size + 1):
        topAns *= i
    for i in range(1, size + 1):
        botAns *= i
    botAns = botAns ** 2
    print(topAns, botAns)
    return int(topAns / botAns)

print(pascal(20))

end = time.clock() - start
print("Time = {0:.2f} seconds".format(end))