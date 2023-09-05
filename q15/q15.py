import math

# Total Paths = (2n)! / (n! * n!)
n = 20
print(int(math.factorial(2*n)/(math.factorial(n)*math.factorial(n))))


