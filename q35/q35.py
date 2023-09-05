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


numCircPrime = 0
for n in range(1_000_000):
    if is_prime(n):
        l = [x for x in str(n)]
        rotationsPrime = [is_prime(int(''.join(l[x:] + l[:x]))) for x in range(len(l))]
        if sum(rotationsPrime)==len(l):
            numCircPrime += 1

    if n%100_000==0:
        print(n)

print("count of circular primes: ",numCircPrime)

