

# create list [2, 3, 5, 7, 11, 13]
# initialize primeIndex at 6
# begin while loop, terminate when primeIndex == 1001
# initialize check variable at list[-1] + 2
# begin for loop with range(len(list))
# compare check variable with all values in list
# if not divisable, append check to list
# if divisable, do nothing.
# after termination of while loop, return list[primeIndex]

def primeNumbers():
    cycles = 0
    primeList = [2, 3, 5, 7, 11, 13]
    checkNum = primeList[-1] + 2
    while len(primeList) < 1002:
        checkNum += 2
        for i in primeList:
            cycles += 1
            if checkNum % i == 0:
                break
            if i == primeList[-1]:
                primeList.append(checkNum)
    print("Cycles = " + str(cycles))
    return primeList

print(primeNumbers())