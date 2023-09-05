multList = [2,3,4,5,6]
for n in range(1,10_000_000):
    nStr = str(n)
    n = int('1'+nStr)
    tmpTuple = [tuple(sorted(str(n*x))) for x in multList]
    tmpTL = len(set(tmpTuple))
    if tmpTL == 1:
        break
print(n)
