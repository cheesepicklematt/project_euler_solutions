import time

t0 = time.time()

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    # Check if the number is divisible by 2 or 3
    if number % 2 == 0 or number % 3 == 0:
        return False
    # Only need to check divisors up to sqrt(number)
    # Any number greater than the square root that divides the number
    # will have a corresponding divisor smaller than the square root.
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def printProgress(i):
    tmpRes = [[sumDict[x]['distinctSum'],x] for x in sumDict]
    try:
        minNum = min([y for x,y in tmpRes if x > stopNum])
        print(i,"smallest number with > 5k solutions: ",minNum)
        return minNum
    except:
        print(i,"most solutions:",max([x for x,y in tmpRes]))
    return 999_999



stopNum = 5000
maxIter = 100
maxNum = 100

nums = [x for x in range(1,maxNum) if is_prime(x)]
sumDict = {x:{'sumLists':[],'distinctSum':0} for x in range(maxNum)}

minSolved = 999_999
solutions = [tuple([n]) for n in nums]
for i in range(maxIter):
    newSolutions = []
    for l in solutions:
        for n in nums:
            tmpSum = sum(l) + n
            if tmpSum < minSolved:
                if tmpSum <  maxNum:
                    tmpL = tuple(sorted(l + tuple([n])))
                    newSolutions.append(tmpL)
                    if tmpL not in sumDict[tmpSum]['sumLists']:
                        sumDict[tmpSum]['sumLists'].append(tmpL)
                        sumDict[tmpSum]['distinctSum'] += 1

    solutions = set(newSolutions)
    minSolved = printProgress(i)


t1 = time.time()

print("first value which can be written as the sum of primes in over five thousand different ways: ",min([y for x,y in [[sumDict[x]['distinctSum'],x] for x in sumDict] if x > stopNum]))
print("run time(s): ",round(t1-t0,3))
