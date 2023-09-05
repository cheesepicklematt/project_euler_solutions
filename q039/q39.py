

ansDict = {x:{'count':0,'sList':[]} for x in range(1,1001)}

for s1 in range(1,1001):
    for s2 in range(1,501):
        for s3 in range(1,251):
            sSorted = [s1, s2, s3]
            sSorted = sorted(sSorted)
            if pow(sSorted[2],2) == pow(sSorted[1],2) + pow(sSorted[0],2):
                p = sum(sSorted)
                if p<1001:
                    if sSorted not in ansDict[p]['sList']:
                        ansDict[p]['count'] += 1 
                        ansDict[p]['sList'].append(sSorted)
    print(s1)



maxCount = 0
for d in ansDict:
    data = ansDict[d]
    count = data['count']
    if count > maxCount:
        maxCount = count
        p = d

print(p)
