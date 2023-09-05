import math
import pandas as pd
import numpy as np

def simplifyFraction(n,d):
    gcd = math.gcd(n, d)
    if gcd==1:
        return n, d
    else:
        return n // gcd, d // gcd

maxD = 12_000

limitMax = 1/2
limitMin = 1/3
res = []
for d in range(2,maxD+1):
    lower = int(np.ceil(d*limitMin))
    upper = int(np.floor(d*limitMax))
    for n in range(lower-1,upper+1):
        decimal = n/d
        if  limitMax > decimal > limitMin:
            f = simplifyFraction(n,d)
            res.append(tuple([f,n/d]))
    if d%1000==0:
        print(d,len(res))

res = list(set(res))
resDF = pd.DataFrame(res,columns=['fraction','decimal'])
resDF = resDF.sort_values(by='decimal').reset_index(drop=True)


print("How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d<=12000:",len(resDF))