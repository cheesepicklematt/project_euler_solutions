import itertools

def getNumLists(maxNum):
    numLists = []
    for n1 in range(1,maxNum):
        for n2 in range(n1+1,maxNum):
            for n3 in range(n2+1,maxNum):
                for n4 in range(n3+1,maxNum):
                    numLists.append(sorted([n1,n2,n3,n4]))

    return numLists

def genGroupIdx(listLen = 4):
    groupTypes = []
    groupS = [[x for y in range(listLen//x)] for x in range(1,listLen)]
    groupS = [y for x in groupS for y in x]
    for c in range(max(groupS)+1):
        for seq in itertools.combinations(groupS,c):
            if sum(seq) == listLen:
                groupTypes.append(seq)

    groupTypes = list(set(groupTypes))
    return [[0]+[sum(x[:i + 1]) for i in range(len(x))] for x in groupTypes]

def genListGroupings(numList):
    groupIdx = genGroupIdx()
    groups = []
    for perm in itertools.permutations(numList):
        for idx in groupIdx:
            groups.append([perm[idx[x-1]:idx[x]] for x in range(1,len(idx))])
    return groups


operators = ['+', '-', '*', '/']
def applyOperatorsToList(lst):
    exprs = []
    for numL in list(itertools.permutations(lst)):
        for oper in list(itertools.product(operators, repeat=len(lst) - 1)):
            exprs.append('('+''.join([str(x)+y for x,y in zip(numL,oper)])+str(numL[-1])+')')
    return exprs

def genAllExprs(groups):
    allExprs = []
    for g in groups:
        subCombo = [applyOperatorsToList(x) for x in g]
        if len(subCombo) == 2:
            for s in list(itertools.product(subCombo[0],subCombo[1])):
                allExprs.append(applyOperatorsToList(s))
        else:
            for s in list(itertools.product(subCombo[0],subCombo[1],subCombo[2])):
                allExprs.append(applyOperatorsToList(s))


    allExprs.append(applyOperatorsToList(numList))

    allExprs = [y for x in allExprs for y in x]
    return list(set(allExprs))

def getConsecutive(results):
    count = 0
    for i in range(1,len(results)+1):
        if i in results:
            count += 1
        else:
            break
    return count

def is_integer(num):
    if isinstance(num, int):
        return True
    elif isinstance(num, float):
        return num.is_integer()
    else:
        return False

def evalExprs(exprs):
    try:
        return eval(exprs)
    except ZeroDivisionError:
        return -99




maxNum = 10

mostConsecutive = 0
for numList in getNumLists(maxNum):
    groups = genListGroupings(numList)
    allExprs = genAllExprs(groups)
    results = [evalExprs(x) for x in allExprs]
    results = list(set([int(x) for x in results if x>0 and is_integer(x)]))

    consecutiveNum = getConsecutive(results)
    if consecutiveNum >  mostConsecutive:
        ans = numList
        mostConsecutive = consecutiveNum

    print(mostConsecutive,consecutiveNum)


print("set of four distinct digits, a<b<c<d, for which the longest set of consecutive positive integers, 1 to n is made:",''.join([str(x) for x in ans]))

