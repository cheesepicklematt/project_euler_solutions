import math
import pandas as pd

def simplifyFraction(n,d):
    gcd = math.gcd(n, d)
    if gcd==1:
        return n, d
    else:
        return n // gcd, d // gcd

maxD = 1_000_000

targetF = 3/7
res = [tuple([(3, 7),targetF])]
for d in range(2,maxD+1):
    for n in range(int(d*targetF),int(d*(targetF*1.00001))):
        decimal = n/d
        if  targetF >= decimal:
            f = simplifyFraction(n,d)
            res.append(tuple([f,n/d]))
    if d%100_000==0:
        print(d,len(res))

res = list(set(res))
resDF = pd.DataFrame(res,columns=['fraction','decimal'])
resDF = resDF.sort_values(by='decimal').reset_index(drop=True)

idx = resDF[resDF['fraction']==(3, 7)].index[0]
ans = resDF.loc[idx-1,'fraction'][0]

print("numerator of the fraction immediately to the left of 3/7:",ans)

