import itertools

permList = [''.join(map(str,n)) for n in itertools.permutations(range(0, 10))]
divList = [2,3,5,7,11,13,17]

pandigitalSum = 0
for n in permList:
    subStr = [int(n[x:x+3]) for x in range(1,8)]
    tmpCount = 0
    for s,d in zip(subStr,divList):
        if s/d%1==0:
            tmpCount += 1
        else:
            break

    if tmpCount == 7:
        pandigitalSum += int(n)

print("sum of pandigital num: ",pandigitalSum)
