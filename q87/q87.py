import time
t0 = time.time()

def SCFpower(s,c,f):
    return s**2 + c**3 + f**4

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

def genPrimeList(maxNum):
    run = True
    primeNum = [2]
    num = 3
    while run:
        if is_prime(num):
            primeNum.append(num)
        if num**2>=maxNum:
            run = False
        num += 2
    return primeNum

maxNum = 50_000_000
primeNum = genPrimeList(maxNum)

ansList = []
for s in primeNum:
    print(s,len(ansList))
    for c in primeNum:
        for f in primeNum:
            ans = SCFpower(s,c,f)
            if ans < maxNum:
                ansList.append(ans)

t1 = time.time()
print("How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power: ",len(set(ansList)))
print("run time(s): ",round(t1-t0,3))
