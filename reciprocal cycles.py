import time
start = time.clock()


def reciprocal_cycles():
    maxCycle = 0
    for divisor in range(1, 1000):
        quotient, cycle = [], []
        remain = 1
        while remain != 0:
            digit, remain = divmod(remain * 10, divisor)
            if len(quotient) > 1:
                if digit in quotient:
                    cycle.append(digit)
                    if len(cycle) > 1 and digit == cycle[0]:
                        if len(cycle) > maxCycle:
                            maxCycle = len(cycle)
                            continue
    return maxCycle

print(reciprocal_cycles())

end = time.clock() - start
print("Time = {0:.2f} seconds".format(end))