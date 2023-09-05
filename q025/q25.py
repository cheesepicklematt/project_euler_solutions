
count = 2
fibSeq = [1,1]
for n in range(10000):
    tmpSum = fibSeq[-1] + fibSeq[-2]
    fibSeq.append(tmpSum)
    count += 1
    if len(str(tmpSum))>=1000:
        break

print(count,tmpSum)