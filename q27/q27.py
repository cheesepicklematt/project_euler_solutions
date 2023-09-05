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

def quad(a,b,n):
    return (n*n) + (a*n) + b

maxConsecutive = 0
for a in range(1000):
    for b in range(1001):
        for i in [-1,1]:
            for j in [-1,1]:
                tmpA = a*i
                tmpB = b*j
                n=0
                run = True
                while run:
                    if is_prime(quad(tmpA,tmpB,n)):
                        n += 1
                    else:
                        run = False
                if n>maxConsecutive:
                    maxConsecutive = n
                    finalA = tmpA
                    finalB = tmpB

print('product of the coefficients to produce max primes: ',finalA*finalB)