import math

def find_factors(n):
    if n==0:
        return []

    factors = []
    # Find factors up to the square root of n
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:  # Add the corresponding factor (except for perfect squares)
                factors.append(n // i)
    factors.sort()
    factors.remove(n)
    return factors

def summable(n, l):
    if n in [x*2 for x in l]:
        return True
    for v in l:
        if n - v in l:
            return True
    return False



abundNum = []
cannotSum = 0
for n in range(28123):
    if not(summable(n,abundNum)):
        cannotSum += n
    if sum(find_factors(n)) > n:
        abundNum.append(n)
    if n%100==0:
        print(n)

print('sum of numbers not a sum of two abundant numbers: ',cannotSum)
