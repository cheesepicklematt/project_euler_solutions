
minN = 2
maxN = 100_000

triNum = [int(x*(x + 1)/2) for x in range(minN,maxN)]
pentNum = [int(x*(3*x - 1)/2) for x in range(minN,maxN)]
hexNum = [int(x*(2*x - 1)) for x in range(minN,maxN)]

nList = []
for i,t in enumerate(triNum):
    if t in pentNum:
        if t in hexNum:
            nList.append(t)
    if len(nList) == 2:
        break
    if i%1000==0:
        print(i)

print('second number that is a triangular, pentagonal and haxagonal: ',nList[1])