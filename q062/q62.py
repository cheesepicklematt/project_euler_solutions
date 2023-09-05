import itertools
import time
t0 = time.time()

def findCubePermutations(lenDict):
    for l in lenDict:
        cubeLst = lenDict[l]
        permDict = {}
        for n in cubeLst:
            sortedN = sorted(list(n))
            sNJoined = ''.join(sortedN)
            if sNJoined in permDict:
                permDict[sNJoined].append(n)
            else:
                permDict[sNJoined] = []
                permDict[sNJoined].append(n)

        for k in permDict:
            if len(permDict[k])==5:
                return permDict[k]
    return False


cubeNum = [str(pow(n,3)) for n in range(1,10_000)]
lenDict = {z:[y for y in cubeNum if len(y)==z] for z in set([len(x) for x in cubeNum])}
t1 = time.time()
print("smallest cube for which exactly five permutations of its digits are cube: ",findCubePermutations(lenDict)[0])
print("run time: ",round(t1-t0,5))

