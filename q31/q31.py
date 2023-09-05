count = 0
for p1 in range(200):
    print(p1)
    for p2 in range(0,200,2):
        for p5 in range(0,200,5):
            for p10 in range(0,200,10):
                for p20 in range(0,200,20):
                    for p50 in range(0,200,50):
                        for p100 in range(0,200,100):
                            tmpSum = p1 + p2 + p5 + p10 + p20 + p50 + p100
                            if tmpSum==200:
                                count += 1

# add 1 for each coin type at the max case
# e.g. 200x1p coin
# 4x50p coin
# 1x200p coin
count += 8

print("Different ways 2 pounds can be made: ",count)
