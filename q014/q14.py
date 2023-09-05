maxLen = 0
for num in range(1,1_000_000,2):
    n = num
    collatzSeq = [n]
    while n>1:
        if n%2==0:
            n = n/2
        else:
            n = (n*3) + 1
        collatzSeq.append(n)
    
    seqLen = len(collatzSeq)
    if seqLen>maxLen:
        print(seqLen,num)
        maxLen = seqLen
        startNum = num

    



