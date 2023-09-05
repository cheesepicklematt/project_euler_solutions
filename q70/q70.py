import pandas as pd
import time

t0 = time.time()

def is_permutation(number1, number2):
    digits1 = sorted(str(number1))
    digits2 = sorted(str(number2))
    return digits1 == digits2


maxFactorSize = 1_000_000
maxN = maxFactorSize*2
factorDict = {x:[] for x in range(1,maxN,2) if x%5!=0}

for f in range(2,maxFactorSize):
    numRange = [x for x in range(f,maxN,f) if x%5!=0 and x%2!=0]
    for n in numRange:
        factorDict[n].append(f)

numNonPrimeList = []
for k in factorDict.keys():
    tmpFact = 0
    for f in factorDict[k]:
        tmpFact += len(range(f,k,f))
    
    numCoPrime = k - tmpFact - 1
    if is_permutation(numCoPrime,k):
        numNonPrimeList.append([k,numCoPrime,k/numCoPrime])


numNonPrimeDF = pd.DataFrame(numNonPrimeList)
numNonPrimeDF.columns = ['num','CoPrimes','Ratio']
t1 = time.time()

print(list(numNonPrimeDF.loc[numNonPrimeDF['Ratio']==numNonPrimeDF['Ratio'].min(),'num'])[0])
print('run time: ',round(t1-t0,2))

numNonPrimeDF.loc[numNonPrimeDF['Ratio']==numNonPrimeDF['Ratio'].min(),:]

# answer 8319823
