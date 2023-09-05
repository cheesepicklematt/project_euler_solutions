from itertools import combinations

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    # Incremental optimization: Check divisibility by 5, then by 7 (5 + 2), then by 11 (7 + 4), and so on
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6 if i % 6 == 5 else 2  # Alternate between 2 and 4
    return True

def isConcatPrime(n1,n2):
    p1 = is_prime(int(n1 + n2))
    if p1==False:
        return False
    p2 = is_prime(int(n2 + n1))
    return all([p1,p2])

def concatNumPrime(lst):
    lstL = len(lst)
    for i in range(lstL):
        for j in range(i+1,lstL):
            if not(isConcatPrime(lst[i],lst[j])):
                return False
    return True


def makesPrime(lst,startLst):
    makesPrime = []
    for k in lst:
        l = startLst+[k]
        if concatNumPrime(l):
            makesPrime.append(k)
    return makesPrime


primeList = [str(x) for x in range(3,10_000,2) if is_prime(x)]
primeList.remove('5')



fivePrimePairs = []
fourPrimePairs = []
count = 0
for n in primeList[0:100]:
    initL = list(primeList)
    initL.remove(n)
    initL = makesPrime(initL,[n])
    currPrimePairs = {}
    currPrimePairs[n] = {'initList':initL}

    for n2 in initL:
        tmpL = list(initL)
        tmpL.remove(n2)
        primes = makesPrime(tmpL,[n2])
        currPrimePairs[n][n2] = {'initList':primes}

    for n2 in initL:
        for n3 in currPrimePairs[n][n2]['initList']:
            tmpL = list(currPrimePairs[n][n2]['initList'])
            primes = makesPrime(tmpL,[n,n2,n3])
            currPrimePairs[n][n2][n3] = {'initList':primes}


    for n2 in initL:
        for n3 in currPrimePairs[n][n2]['initList']:
            for n4 in currPrimePairs[n][n2][n3]['initList']:
                tmpL = list(currPrimePairs[n][n2][n3]['initList'])
                primes = makesPrime(tmpL,[n,n2,n3,n4])
                currPrimePairs[n][n2][n3][n4] = {'initList':primes}
                if tmpL!=[]:
                    fourPrimePairs.append(tuple(sorted([n,n2,n3,n4])))

    for n2 in initL:
        for n3 in currPrimePairs[n][n2]['initList']:
            for n4 in currPrimePairs[n][n2][n3]['initList']:
                for n5 in currPrimePairs[n][n2][n3][n4]['initList']:
                    tmpL = list(currPrimePairs[n][n2][n3]['initList'])
                    primes = makesPrime(tmpL,[n,n2,n3,n4,n5])
                    currPrimePairs[n][n2][n3][n5] = {'initList':primes}
                    if tmpL!=[]:
                        fivePrimePairs.append(tuple(sorted([n,n2,n3,n4,n5])))

        count += 1
        if count%10==0:
            print(count)

fourPrimePairs = list(set(fourPrimePairs))
fivePrimePairs = list(set(fivePrimePairs))

[sum([int(y) for y in x]) for x in fivePrimePairs]

