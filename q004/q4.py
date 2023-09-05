

def isPalindromic(n):
    n = str(n)
    n_r = n[::-1]
    return n==n_r

palNum = 0
for x in range(100,1000):
    for y in range(100,1000):
        m = x*y
        if isPalindromic(m):
            if m>palNum:
                palNum = m



print(palNum)

