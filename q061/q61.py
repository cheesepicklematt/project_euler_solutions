import itertools
import numpy as np 
import time

t0 = time.time()

def createStartEndDict(lst):
    startList = list(set([x[:2] for x in lst]))
    endList = list(set([x[2:] for x in lst]))

    endDict = {x:[] for x in endList}
    startDict = {x:[] for x in startList}
    for n in lst:
        end = n[2:]
        start = n[:2]
        endDict[end].append(n)
        startDict[start].append(n)

    return {"endDict":endDict,"startDict":startDict}

def isCyclical(lst):
    for i in range(len(lst)-1):
        nStr = str(lst[i])
        nStr_p = str(lst[i-1])
        nStr_n = str(lst[i+1])

        if nStr[:2]!=nStr_p[-2:]:
            return False
        if nStr[-2:]!=nStr_n[:2]:
            return False
    return True


def getPossibleChains(keys,sn):
    nLst = [[sn]]
    for key in keys:
        startDict = fullDict_startEnd[key]['startDict']
        nextLst = []
        for n in nLst:
            nLst_last = n[-1]
            nEnd = nLst_last[2:]
            if nEnd in startDict.keys():
                nextLst.append([n + [x] for x in startDict[nEnd] if x!=nLst_last])
            else:
                break
        if nextLst == [[]] or nextLst == []:
            break
        else:
            nextLst = [y for x in nextLst for y in x]
            nLst = nextLst
    return nLst

nIter = 400
triNum = [y for y in [str(int(x*(x+1)/2)) for x in range(nIter)] if len(str(y))==4]
sqNum = [y for y in [str(int(x*x)) for x in range(nIter)] if len(str(y))==4]
pentNum = [y for y in [str(int(x*((3*x)-1)/2)) for x in range(nIter)] if len(str(y))==4]
hexNum = [y for y in [str(int(x*((2*x)-1))) for x in range(nIter)] if len(str(y))==4]
heptNum = [y for y in [str(int(x*((5*x)-3)/2)) for x in range(nIter)] if len(str(y))==4]
octNum = [y for y in [str(int(x*((3*x)-2))) for x in range(nIter)] if len(str(y))==4]



fullDict = {
    'triNum':triNum, 
    'sqNum':sqNum,
    'pentNum':pentNum,
    'hexNum':hexNum,
    'heptNum':heptNum,
    'octNum':octNum
}
fullDict_startEnd = {x:createStartEndDict(fullDict[x]) for x in fullDict.keys()}


results = []
for mk in fullDict:
    print(mk)
    numList = fullDict[mk]
    tmpFd = dict(fullDict)
    a = tmpFd.pop(mk,None)
    allKeys = list(itertools.permutations(tmpFd.keys()))
    for sn in numList:
        for keys in allKeys:
            tmpAns = getPossibleChains(keys,sn)
            results.append(tmpAns)




cycLists = [y for y in [list(x[0]) for x in results] if isCyclical(y) and len(y)==6]
t1 = time.time()

print("sum of the only ordered set of six cyclic 4-digit numbers: ",sum([int(x) for x in cycLists[0]]))
print("run time: ",round(t1-t0,2))

