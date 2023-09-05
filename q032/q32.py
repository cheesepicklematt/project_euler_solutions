target = sorted('123456789')
pandigital = []
for a in range(1,99):
    for b in range(100,10_000):
        tmpMult = a*b
        fullStr = str(a)+str(b)+str(tmpMult)
        if len(fullStr)!=9:
            pass
        else:
            if sorted(fullStr)==target:
                pandigital.append([tmpMult,a,b])

print("sum of all products whose multiplicand/multiplier/product identity is pandigital (1-9): ",sum(set([x[0] for x in pandigital])))
