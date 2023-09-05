powerVals = []
for a in range(2,101):
    for b in range(2,101):
        powerVals.append(pow(a,b))

print("distinct terms: ",len(set(powerVals)))

