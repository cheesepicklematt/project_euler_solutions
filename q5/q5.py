import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def getLCM(maxNum):
    tmp = 1
    for i in range(2, maxNum+1):
        tmp = lcm(tmp, i)

    return tmp

LCM20 = getLCM(20)