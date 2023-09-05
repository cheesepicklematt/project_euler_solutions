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

primeList = [x for x in range(10_000) if is_prime(x)]
maxConsec = 0
for l in range(1,len(primeList)):
    tmpLists = [primeList[l:l+x] for x in range(1,len(primeList)+1-l)]
    for lst in tmpLists:
        lstLen = len(lst)
        lstSum = sum(lst)
        if lstSum<1_000_000:
            if lstLen>maxConsec:
                if is_prime(lstSum):
                    maxConsec = lstLen
                    fLst = lst

print("sum of max consecutive primes: ",sum(fLst))