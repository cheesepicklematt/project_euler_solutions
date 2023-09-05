import math

def find_factors(n):
    factors = []
    # Find factors up to the square root of n
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:  # Add the corresponding factor (except for perfect squares)
                factors.append(n // i)
    factors.sort()
    try:
        factors.remove(1)
        factors.remove(n)
    except:
        pass
    return factors

def sum2N(n):
    return n*(n+1)/2

for n in range(20_000):
    triNum = int(sum2N(n))
    if len(find_factors(triNum))>500:
        print(triNum)
        break


