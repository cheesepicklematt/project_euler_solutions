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
        factors.remove(n)
    except:
        pass
    return factors

amiNum = []
for n in range(10000):
    aSum = sum(find_factors(n))
    bSum = sum(find_factors(aSum))
    if bSum==n and n!=aSum:
        amiNum.append(aSum)
        amiNum.append(bSum)


print("sum of amicable numbers: ",sum(set(amiNum)))


