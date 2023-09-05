run = True
fibNum = [1,2]
count = 1
evenSum = 2
while run:
    n = fibNum[count] + fibNum[count-1]
    fibNum.append(n)
    count += 1
    if n>4_000_000:
        run = False
    else:
        if n%2==0:
            evenSum += n

print(evenSum)

