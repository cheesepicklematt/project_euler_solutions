import time

t0 = time.time()

maxLen = 1_500_000
maxIter = int(maxLen**0.5)
lenDict = {x:set() for x in range(1,maxLen+1)}

for m in range(2,maxIter+1):
    for n in range(1,m):
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2

        mult = 1
        while True:
            ai = a*mult
            bi = b*mult
            ci = c*mult

            tLst = tuple(sorted([ai, bi, ci]))
            tSum = sum(tLst)
            if tSum > maxLen:
                break
            else:
                lenDict[tSum].add(tLst)
            mult += 1
        
    if m % 100 == 0:
        print(m)


t1 = time.time()

print("Given that L is the length of the wire, for how many values of L<=1_500_00 can exactly one integer sided right angle triangle be formed:",sum([len(lenDict[x])==1 for x in lenDict]))
print("run time(s): ",round(t1-t0,3))

