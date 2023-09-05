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

def genPossiblePrimes(maxNum):
    # 1 is not a prime
    # 2 is the only even prime
    # 5 is the only prime divisible by 5
    return [2,3,5] + [x for x in range(7,maxNum,2) if x%5!=0]


checkList = genPossiblePrimes(1_999_999)
sum([n for n in checkList if is_prime(n)])