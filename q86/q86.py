import time

# check if (c) sqrt(a^2 + b^2) is an integer
def isTriplet(a,b):
    cS = a**2 + b**2
    cSR = int(cS**0.5)
    if cSR*cSR == cS:
        return True
    return False

tS = time.time()

numTriplets = 0
w = 1
while numTriplets<1_000_000:
    bTripDict = {x:isTriplet(w,x) for x in range(1,(w*2)+1)}
    for h in range(1,w+1):
        for l in range(h,w+1):
            if bTripDict[h+l]: 
                numTriplets += 1
    w += 1

    if w%100==0:
        print(w,numTriplets)
    

tE = time.time()

print("least value of M such that the number of solutions first exceeds one million:",w-1)
print("run time: ",round(tE-tS,3))

