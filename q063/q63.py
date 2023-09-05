res = []
for n in range(1,100):
    for p in range(100):
        tmpA = pow(n,p)
        if len(str(tmpA)) == p:
            res.append([n,p,tmpA])

print("How many n-digit positive integers exist which are also an n-th power: ",len(set([x[-1] for x in res])))