sideLen = 0
prevSq = [1]
spiralNum = [1]
run = True
while run:
    sideLen += 2
    totalNum = sideLen*4
    numList = [x for x in range(max(prevSq)+1,max(prevSq)+totalNum+1)]
    numListSplit = [numList[sideLen*(x):sideLen*(x+1)] for x in range(4)]
    spiralNum.append(sum([x[-1] for x in numListSplit]))

    prevSq = prevSq + numList

    if sideLen+1 == 1001:
        run = False

print("sum of spiral numbers: ",sum(spiralNum))