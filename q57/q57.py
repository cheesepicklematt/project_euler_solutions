count = 0
for _ in range(1000):
    nextNum = ((2*den) + num)
    nextDen = num + den
    if len(str(nextNum)) > len(str(nextDen)):
        count += 1

    num = nextNum
    den = nextDen
