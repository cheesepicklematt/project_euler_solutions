import itertools


def getPossibleIdx(nStr):
    idxLst = [x for x in range(len(nStr)-1)]
    if len(idxLst)==1:
        return [idxLst]
    allIdx = []
    for x in range(1,len(idxLst)+1):
        allIdx += list(itertools.combinations(idxLst, x))
    return allIdx


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

def replaceStrIdx(string,idx,newStr):
    return string[:idx] + newStr + string[idx + 1:]


def countPrimes(nStr,d,numPrimes):
    exitNum = 10 - numPrimes
    primeLst = []
    count = 0
    badCount = 0
    start = 1 if d[0]==0 else 0
    for x in range(start,10):
        tmp = nStr
        for i in d:
            tmp = replaceStrIdx(tmp,i,str(x))

        if is_prime(int(tmp)):
            count += 1
            primeLst.append(int(tmp))
        else:
            badCount += 1
            if badCount > exitNum:
                return False, False

    return count, tuple(primeLst)

numPrimes = 8
primeSets = []
for n in range(11,150_000,2):
    nStr = str(n)
    if nStr[-1]!='5':
        tmpD = getPossibleIdx(nStr)
        for d in tmpD:
            count, pLst = countPrimes(nStr,d,numPrimes)
            if count == numPrimes and pLst not in primeSets:
                primeSets.append(pLst)

    if len(primeSets)>0:
        break


print("smallest prime in set: ",primeSets[0][0])

