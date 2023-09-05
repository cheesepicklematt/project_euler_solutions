import math


def has_integer_square_root(number):
    sqrt = int(number ** 0.5)
    return sqrt * sqrt == number

def solveEquation(d):
    maxIter = 5_000_000
    for y in range(1,maxIter):
        tmpNum = 1+d*(y**2)
        if has_integer_square_root(tmpNum):
            x = math.sqrt(tmpNum)
            return [int(x),y,d]
    return False

sqVal = [x**2 for x in range(40)]
dVal = [x for x in range(2,1000) if x not in sqVal]

trueSolv = []
for d in dVal:
    tmpSol = solveEquation(d)
    if tmpSol==False:
        print(d)
    else:
        trueSolv.append(tmpSol)
    






solveEquation(62)
[[x,y*d] for x,y,d in trueSolv]




def solveEquation(d):
    maxIter = 10_000
    for y in range(1,int(maxIter/2)):
        for x in range((y*2)-1,min(maxIter,int(y*d))):
            ans = x**2 - (d*(y**2))
            if ans==1:
                return [x,y,d]
    return False
    #minX = min([x[0] for x in res])
    #return [x for x in res if x[0]==minX][0]
