import math

def combinations(n,r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

count = 0
for n in range(1,101):
    for r in range(1,n+1):
        tmp = combinations(n,r)
        if tmp > 1_000_000:
            count += 1

