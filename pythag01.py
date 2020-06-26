

import math

def pythagTrip():
    for i in range(290, 500):
        if (1000 * i - 500000) % (i - 1000) == 0:
            j = int((1000 * i - 500000) / (i - 1000))
            c = int(math.sqrt(i**2 + j**2))
            return (i * j * c)



print(pythagTrip())