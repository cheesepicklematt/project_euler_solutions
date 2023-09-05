n = 100
possibleSums = [1]+[0 for x in range(n)]
for i in range(1,n):
    for j in range(i,n+1):
        possibleSums[j] += possibleSums[j-i]

print("How many different ways can one hundred be written as a sum of at least two positive integers:",possibleSums[n])
