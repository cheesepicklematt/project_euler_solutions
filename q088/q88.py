import itertools
import math
import numpy as np

def prime_factors(n):
    factors = []
    # Handle even numbers
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Handle odd divisors
    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 2  # Skip even numbers as divisors
    # If n is a prime greater than 2
    if n > 2:
        factors.append(n)
    return factors

def sameElements(l):
    first_element = l[0]
    return all(element == first_element for element in l)

def cumSumListofLists(ll):
    return [[sum(x[:i + 1]) for i in range(len(x))] for x in ll]

def getGroupIdx(l):
    t = []
    groupS = [[x for y in range(len(l)//x)] for x in range(1,len(l))]
    groupS = [y for x in groupS for y in x]
    if len(l)>=3:
        for _ in range(3):
            groupS.remove(1) # remove 1 because the all 1's case is manually added
        groupS.remove(max(groupS)) # remove max number. Case manually added below

        ###   manual appends   ###
        # case for all 1's and 2
        tmpList = [1 for x in range(len(l)-1)]
        tmpList.append(2)
        t.append(tuple(tmpList))
        # case for 1 and len(l)-1 (largest group)
        t.append(tuple([1,len(l)-1]))

    lLen = len(l)
    for i in range(len(l)-2, 1, -1):
        for seq in list(set(itertools.combinations(groupS, i))):
            if sum(seq)==lLen:
                t.append(tuple(sorted(seq)))
    
    ###   manual appends   ###
    # case for all 1's
    t.append(tuple([1 for x in range(len(l))]))
    return list(set(t))


def getAllListComb(l):
    groups = getGroupIdx(l)
    groupIdx = [[0]+x for x in cumSumListofLists(groups)]
    if sameElements(l):
        perm = [l]
    else:
        perm = list(set(itertools.permutations(l)))

    tmpG = []
    for tmpList in perm:
        for idx in groupIdx:
            rawGroups = [tmpList[idx[x-1]:idx[x]] for x in range(1,len(idx))]
            count = 0
            for _ in range(len(rawGroups)):
                t = list(np.hstack([math.prod(x) if j<=count else x for j,x in enumerate(rawGroups)]))
                tmpG.append(tuple(sorted(t)))
                count += 1
 
    return list(set(tmpG))



limit = 12000
solDict = {k:999_999_999 for k in range(2,limit*2)}

for n in range(4,limit+280):
    pf = prime_factors(n)
    fullList = getAllListComb(pf)

    if len(fullList[0])!=1:
        for f in fullList:
            f = list(f)
            diff = n - sum(f)
            if diff!=0:
                sol = f + [1]*diff
            else:
                sol = f
            tmpAns = sum(sol)
            idx = len(sol)

            if tmpAns<solDict[idx]:
                solDict[idx] = tmpAns

    if n%10==0:
        print(n)

t = set([solDict[x] for x in solDict if x<=limit])
print("sum of all the minimal product-sum numbers for 2 <= k <= 12000: ",sum(t))










