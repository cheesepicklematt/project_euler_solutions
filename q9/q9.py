import math

ans = 'None'
for a in range(1000):
    for b in range(1000):
        aSq = a*a
        bSq = b*b
        c = math.sqrt(aSq+bSq)
        if c%1==0 and a<b<c and a + b + c == 1000:
            ans = [a,b,c]

math.prod(ans)