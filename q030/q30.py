limit = sum([pow(int(x),5) for x in str(999_999)])
numList = []
for n in range(2,limit):
    tmpSum = sum([pow(int(x),5) for x in str(n)])
    if tmpSum == n:
        numList.append(n)

print("sum of all the numbers that can be written as the sum of fifth powers of their digits: ",sum(numList))