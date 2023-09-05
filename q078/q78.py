
import time

t0 = time.time()
maxNum = 1_000_000
divNum = 1_000_000

pentNum = []
for kr in range(1,maxNum):
    for m in [1,-1]:
        k = kr * m
        pentNum.append(k*(3*k - 1)//2)


possibleSums = [1]+[0 for x in range(maxNum)]

for n in range(1,maxNum):
    for k in range(1,len(pentNum)):
        t1 = (-1)**((k-1)//2) # need t1 to be +,+,-,-,+,+,-,-
        t2s = n-pentNum[k-1]
        if t2s<0:
            break
        t2 = possibleSums[t2s]
        possibleSums[n] += t1*t2

    if possibleSums[n] % divNum == 0:
        break

t1 = time.time()

print("Find the least value of n for which p(n) is divisible by one million:",n)
print("run time(s): ",round(t1-t0,3))
