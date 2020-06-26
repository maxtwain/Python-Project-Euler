import math, time
start = time.clock()

def largestCollatz():
    maxSeq = [0,0]
    for startNumber in range(1000000, 500000, -1):
        i = startNumber
        seq = 1
        while i - 1:
            if not i % 2:
                i = int(i / 2)
            else:
                i = 3 * i + 1
            seq += 1
        if seq > maxSeq[1]:
            maxSeq[0], maxSeq[1] = startNumber, seq
    return maxSeq

def cacheCollatz():
    prevPairs = {}
    maxSeq = [0,0]
    for startNumber in range(500000, 1000000):
        i = startNumber
        seq = 1
        while i - 1:
            i = int(i / 2) if not i % 2 else 3 * i + 1
            if i in prevPairs:
                seq += prevPairs[i]
                break
            seq += 1
        prevPairs[startNumber] = seq
        if seq > maxSeq[1]:
            maxSeq[0], maxSeq[1] = startNumber, seq
    return maxSeq

print(cacheCollatz())

end = time.clock() - start
print("Time = {0:.2f} seconds".format(end))