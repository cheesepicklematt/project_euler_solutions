import collections
import math
import time

t0 = time.time()

def getY(x):
    return g*x - g*qx + qy

def getX(y):
    return (y + g*qx - qy)/g


def getCoordinates(g,qy,qx):
    yCoo = [z for z in [(getY(x),x) for x in xyVal] if z[0]>=xyVal[0] and z[0]<=xyVal[1]]
    xCoo = [z for z in [(y,getX(y)) for y in xyVal] if z[1]>=xyVal[0] and z[1]<=xyVal[1]]
    return list(set(yCoo + xCoo))

def sortedTup(yx1,yx2):
    return tuple(sorted([yx1,yx2]))

def is_almost_integer(number, tolerance=1e-10):
    return abs(number - round(number)) < tolerance
    

maxLen = 50

loopMax = maxLen + 1
xyVal = [0,maxLen]
cooDict = collections.defaultdict(set)
for y in range(1,loopMax):
    c1 = (y,0)
    for x in range(1,loopMax):
        co1 = (y,x)
        co2 = (0,x)
        cooDict['co'].add(sortedTup(c1,co1))
        cooDict['co'].add(sortedTup(c1,co2))

for x in range(1,loopMax):
    c1 = (0,x)
    for y in range(1,loopMax):
        co1 = (y,x)
        co2 = (y,0)
        cooDict['co'].add(sortedTup(c1,co1))
        cooDict['co'].add(sortedTup(c1,co2))



for qy in range(1,loopMax):
    for qx in range(1,loopMax):
        g = -1/(qy/qx)

        intercept = getCoordinates(g,qy,qx)
        if len(intercept)>1:
            minX = math.floor(min([intercept[0][1],intercept[1][1]]))
            maxX = math.floor(max([intercept[0][1],intercept[1][1]]))

            cooList = [(int(z),a) for z,a in [(getY(x),x) for x in range(minX,maxX+1)] if is_almost_integer(z)]
            for z in cooList:
                if (qy,qx)!=(z) and z[0] <= maxLen and z[1] <= maxLen:
                    cooDict['co'].add(sortedTup((qy,qx),(z)))
                

t1 = time.time()
print("how many right triangles can be formed:",len(cooDict['co']))
print("run time(s): ",round(t1-t0,6))

