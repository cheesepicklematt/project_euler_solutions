def get_prime_factors(number):
    factors = []
    divisor = 2

    while divisor * divisor <= number:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1

    if number > 1:
        factors.append(number)

    return factors


numFact = 4
for n in range(1_000_000):
    count = 0
    for x in range(n,n+numFact):
        if len(set(get_prime_factors(x))) == numFact:
            count += 1
        else:
            break
    if count == numFact:
        break

print("first of four consecutive integers to have four distinct prime factors each: ",n)

