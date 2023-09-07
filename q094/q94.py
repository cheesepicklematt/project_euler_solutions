import time

t0 = time.time()

def returnP(a,b,c):
    base1 = a*2
    base2 = b*2

    diff1 = abs(base1-c)
    diff2 = abs(base2-c)

    if diff1 == 1 or diff2 == 1:
        if diff1 == 1:
            p = base1 + c*2
            if p<maxP:
                return p

        if diff2 == 1:
            p = base2 + c*2
            if p<maxP:
                return p
    return 0


maxP = 1_000_000_000



maxSLen = maxP//3
maxIter = int(maxSLen**0.5)
totalP = 0
tmp = []
for m in range(2,maxIter+1):
    # get n values by solving Euclid's formula for a Pythagorean triple
    n1 = int(((1-m**2)/-3)**0.5)
    n2 = int(2*m - (3*(m)**2 - 1)**0.5)
    for n in [n1,n2]:
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2

        totalP += returnP(a,b,c)


t1 = time.time()

print("Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion:",totalP)
print("run time(s): ",round(t1-t0,6))
