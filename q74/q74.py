import math
import time

factorialCashe = {str(n):math.factorial(n) for n in range(10)}

def numFactSum(n):
    nStr = str(n)
    return sum([casheFactorial(x) for x in nStr])

def getNonRecurrLen(nS):
    numDict = {nS:nS}
    n = nS
    while True:
        nFact = numFactSum(n)
        if nFact in numDict:
            break
        numDict[nFact] = nFact
        n = nFact
    return len(numDict)

ansList = []
for nS in range(1,1_000_000):
    ansList.append(getNonRecurrLen(nS))
    if nS%100_000==0:
        print(nS)


print("How many chains, with a starting number below one million, contain exactly sixty non-repeating terms:",sum([n==60 for n in ansList]))

