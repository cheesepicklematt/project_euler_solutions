

maxSum = 0
for a in range(100):
    for b in range(100):
        tmpSum = sum([int(x) for x in str(pow(a,b))])
        if tmpSum > maxSum:
            maxSum = tmpSum