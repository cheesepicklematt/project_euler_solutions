
digits_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

maxPanMult = 0
for n in range(1,10_000):
    for nLMax in range(10):
        tmpStr = ''.join([str(x*n) for x in range(1,nLMax)])
        if digits_set.issubset(tmpStr) and len(tmpStr) == 9:
            tmpStr = int(tmpStr)
            if tmpStr > maxPanMult:
                maxPanMult = tmpStr


print("largest pandigital (1-9) number: ",maxPanMult)
