def find_factors(n):
    import math
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


n = 600851475143
max([x for x in find_factors(n) if is_prime(x)])