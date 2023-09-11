import collections

def isRightTriangle(c1,c2):
    y2,x2 = c1
    y3,x3 = c2
    a = (int(pow((x2 - 0), 2)) + int(pow((y2 - 0), 2)))
    b = (int(pow((x3 - x2), 2)) + int(pow((y3 - y2), 2)))
    c = (int(pow((x3 - 0), 2)) + int(pow((y3 - 0), 2)))

    if (a == b+c) or (b == a + c) or (c == a + b):
        return True
    else:
        return False

def sortedTup(yx1,yx2):
    return tuple(sorted([yx1,yx2]))


maxLen = 50
loopMax = maxLen + 1

cooDict_bf = collections.defaultdict(set)

for y2 in range(0,loopMax):
    for x2 in range(0,loopMax):
        for y3 in range(0,loopMax):
            for x3 in range(0,loopMax):
                c1 = (y2,x2)
                c2 = (y3,x3)
                if c1 != c2 and c1 != (0,0) and c2 != (0,0):
                    if isRightTriangle(c1,c2):
                        co = sortedTup(c1,c2)
                        cooDict_bf['co'].add(co)
    print(y2)


print("how many right triangles can be formed:",len(cooDict_bf['co']))
