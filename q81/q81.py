import os
import numpy as np

a = open(os.path.join('euler','q81','0081_matrix.txt')).read()
a = [[int(y) for y in x.split(',')] for x in a.split('\n') if x!='']

# init array. Edges will just be a cumulative sum
costA = np.array(a)
costA[0] = np.cumsum(costA[0])
costA[:,0] = np.cumsum(costA[:,0])


for x in range(1,len(costA)):
    for y in range(1,len(costA)):
        currCost = costA[y,x]
        topSum = currCost + costA[y-1,x]
        leftSum = currCost + costA[y,x-1]
        newCost = min(topSum,leftSum)
        costA[y,x] = newCost

print(costA[-1,-1])

