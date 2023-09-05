import itertools

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


maxPrimePanDigit = 0
for n in range(10,5,-1):
    pdNum = list(itertools.permutations(range(1, n)))
    pdNum.reverse()
    print(len(pdNum))
    for y in pdNum:
        nInt = int(''.join(map(str,y)))
        if nInt>maxPrimePanDigit:
            if is_prime(nInt):
                maxPrimePanDigit = nInt

print("max pandigital prime: ",maxPrimePanDigit)