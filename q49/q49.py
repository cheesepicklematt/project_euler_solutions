def find_arithmetic_sequences(lst):
    sequences = []
    n = len(lst)

    for i in range(n):
        for j in range(i+1, n):
            common_difference = lst[j] - lst[i]
            sequence = [lst[i], lst[j]]

            for k in range(j+1, n):
                if lst[k] - sequence[-1] == common_difference:
                    sequence.append(lst[k])

            if len(sequence) >= 3:
                sequences.append(sequence)

    return sequences


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

primeList = []
for n in range(1000,10_000):
    if is_prime(n):
        primeList.append(n)


sortedPrimes = {''.join(sorted(str(x))):[] for x in primeList}
for p in primeList:
    sortedP = ''.join(sorted(str(p)))
    sortedPrimes[sortedP].append(p)


permPrimes = [sortedPrimes[x] for x in sortedPrimes if len(sortedPrimes[x])>=3]
seq = []
for p in permPrimes:
    tmp = find_arithmetic_sequences(p)
    if len(tmp)>0:
        seq.append(tmp)
    #[j-i for i, j in zip(p[:-1], p[1:])]


print("ans: ",''.join([str(x) for x in seq[1][0]]))



