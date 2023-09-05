


maxLen = 2
loopMax = maxLen + 1


count = 0
coo = []

a = (0,0)
for y in range(0,loopMax):
    for x in range(0,loopMax):
        if y != 0 or x != 0:
            if y == 0:
                count += maxLen
            if x == 0:
                count += maxLen
