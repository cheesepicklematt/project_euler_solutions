def getRecurrLen(denom):
    remainderDict = {}
    remainder = 1
    pos = 0
    while remainder!=0:
        _,remainder = divmod(remainder*10,denom)

        if remainder in remainderDict:
            return pos - remainderDict[remainder]
        
        remainderDict[remainder] = pos
        pos += 1

    return 0

maxLen = 0
for n in range(1,1000):
    tmpLen = getRecurrLen(n)
    if tmpLen>maxLen:
        maxLen = tmpLen
        maxLenNum = n

print("longest recurring cycle: ",maxLenNum)