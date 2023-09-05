
def isPalindromic(n):
    n = str(n)
    n_r = n[::-1]
    return n==n_r


lychList = []

numLych = 0
for n in range(1,10_001):
    nI = n
    for i in range(50):
        nStr = str(nI)
        nStr_r = nStr[::-1]
        nI =  nI + int(nStr_r)
        if isPalindromic(nI):
            break

    if i == 49:
        numLych += 1
        lychList.append([n,i])






