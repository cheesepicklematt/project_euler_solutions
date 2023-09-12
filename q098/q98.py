import os
import collections 
import itertools
import time

t0 = time.time()

def getAnagPairs():
    words = open(os.path.join('q098','0098_words.txt')).read()
    words = [x.replace('"','') for x in words.split(',')]


    anagramDict = collections.defaultdict(list)

    for w in words:
        sortedW = ''.join(sorted(list(w)))
        anagramDict[sortedW].append(w)

    anagPairs = []
    for k in anagramDict:
        dictVal = anagramDict[k]
        if len(dictVal) >= 2:
            anagPairs.append(list(itertools.combinations(dictVal,2)))

    return [y for x in anagPairs for y in x]

def mapPList(pList):
    return ''.join([mapping[x] for x in pList])

def isSqNum(pList):
    n = mapPList(pList)
    if n[0] == '0':
        return False
    n = int(n)
    if n in sqNumList:
        return True
    return False



numList = [str(x) for x in range(10)]
sqNumList = {x**2:x**2 for x in range(100_000) if x**2<=9876543210}
anagPairs = getAnagPairs()
permDict = {x:list(itertools.permutations(numList,x)) for x in set([len(set(list(p[0]))) for p in anagPairs])}

anagSq = []
for p in anagPairs:
    print(p)
    pList_1 = list(p[0])
    pList_2 = list(p[1])
    uniqLetters = set(pList_1)

    tmpPerm = permDict[len(uniqLetters)]
    for tp in tmpPerm:
        mapping = {y:x for x,y in zip(tp,uniqLetters)}
        if isSqNum(pList_1):
            if isSqNum(pList_2):
                sq1 = mapPList(pList_1)
                sq2 = mapPList(pList_2)
                anagSq.append([mapping,p,sq1,sq2])

t1 = time.time()

print("largest square number formed: ",max([max([int(c),int(d)]) for a,b,c,d in anagSq]))
print("run time(s): ",round(t1-t0,3))
