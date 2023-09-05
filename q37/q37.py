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

n = 11
count = 0
tSum = 0
run = True
while run:
    if is_prime(n):
        nStr = str(n)
        l2r = [is_prime(int(nStr[x:])) for x in range(len(nStr))]
        r2l = [is_prime(int(nStr[:x+1])) for x in range(len(nStr)-1)]
        if (all(l2r) + all(r2l)) == 2:
            count += 1
            tSum += n
            if count==11:
                run = False
    n += 2

print("sum of truncatabe primes left to right: ",tSum)