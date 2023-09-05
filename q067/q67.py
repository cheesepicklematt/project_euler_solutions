import os
import numpy as np
import time

t0 = time.time()
triangle_raw = open(os.path.join('euler','q67','0067_triangle.txt')).read()
triangle = [[int(y) for y in x.split(' ')] for x in triangle_raw.split('\n') if x!='']
colLen = len(triangle)
triangleSq = [x+[0 for y in range(colLen-len(x))] for x in triangle]

for r in range(len(triangle)-2,-1,-1):
    sumList = [x for x in triangleSq[r] if x!=0]
    newRow = []
    for i,n in enumerate(sumList):
        leftSum = n+triangleSq[r+1][i]
        rightSum = n+triangleSq[r+1][i+1]
        newRow.append(max(leftSum,rightSum))
    triangleSq[r] = newRow + [0 for x in range(colLen - len(newRow))]


print(triangleSq[0][0])
t1 = time.time()
print(t1-t0)