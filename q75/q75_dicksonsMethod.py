
def factors(n):    
    return set((i, n // i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)

maxLen = 1_500_000
maxIter = 300_000
lenDict = {x:0 for x in range(1,maxLen+1)}

for r in range(2,maxIter,2):
    rS = r**2
    tsVal = [x for x in factors(rS/2) if sum(x)+r<maxLen]
    for t,s in tsVal:
        a = r + s
        b = r + t
        c = r + s + t
        tLen = a + b + c
        if tLen <= maxLen:
            lenDict[tLen] += 1

    if r % 10_000 == 0:
        print(r)




print("Given that L is the length of the wire, for how many values of L<=1_500_00 can exactly one integer sided right angle triangle be formed:",sum([lenDict[x]==1 for x in lenDict]))
