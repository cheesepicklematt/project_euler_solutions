
def countRelativelyPrimeNumbers(n):
    '''
    counts number of relatively prime numbers for each number up to n
    '''
    phi = [i for i in range(n + 1)]
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    return phi

n = 1_000_000
ans = countRelativelyPrimeNumbers(n)

# answer will be the sum of the relatively prime numbers for each number
# all other fractions can be simplified to a fraction already counted
print("count of set of fractions: ",sum(ans[2:]))