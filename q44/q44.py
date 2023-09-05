maxP = 3000
minP = 1000
pentNum = [int(x*(3*x - 1)/2) for x in range(minP,maxP)]

minDiff = 999_999_999
for pj in pentNum:
    for pk in pentNum:
        tmpDiff = abs(pk - pj)
        if tmpDiff < minDiff:
            tmpSum = pk + pj
            sumInPent = True if tmpSum in pentNum else False
            diffInPent = True if tmpDiff in pentNum else False
            if sumInPent and diffInPent:
                minDiff = tmpDiff

print("minimum difference: ",minDiff)
