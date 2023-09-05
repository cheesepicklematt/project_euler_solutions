
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    # Check if the number is divisible by 2 or 3
    if number % 2 == 0 or number % 3 == 0:
        return False
    # Only need to check divisors up to sqrt(number)
    # Any number greater than the square root that divides the number
    # will have a corresponding divisor smaller than the square root.
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

maxN = 10_000
maxTS = 100
twoSqNum = [2*(x**2) for x in range(1,maxTS)]
primeNum = [x for x in range(1,maxN,2) if is_prime(x)]

for n in range(9,maxN,2):
    if not(is_prime(n)):
        count = 0
        for ts in twoSqNum:
            tmpDiff = n - ts
            if  tmpDiff in primeNum:
                count += 1
        if count == 0:
            break

print('smallest composite prime: ',n)




