import math

limit = 3_000_000
tSum = 0
for n in range(3,limit):
    tmpSum = sum([math.factorial(int(x)) for x in str(n)])
    if tmpSum==n:
        tSum += n


print("sum of all numbers which are equal to the sum of the factorial of their digits: ",tSum)