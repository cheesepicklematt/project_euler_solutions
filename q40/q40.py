import math
numList = [
    1,
    10,
    100,
    1_000,
    10_000,
    100_000,
    1_000_000
]
numStr = ''.join([str(x) for x in range(1_000_000)])
print("ans: ",math.prod([int(numStr[x]) for x in numList]))
