
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

sideLen = 0
numPrime = 0
numDiag = 1
prevSqMax = 1
run = True
while run:
    sideLen += 2
    totalNum = sideLen*4
    numList = [x for x in range(prevSqMax+1,prevSqMax+totalNum+1)]
    numListSplit = [numList[sideLen*(x):sideLen*(x+1)] for x in range(4)]

    numPrime += sum([is_prime(x[-1]) for x in numListSplit])
    numDiag += 4
    prevSqMax = max([prevSqMax] + numList)
    if numPrime/numDiag < 0.1:
        run = False
    if sideLen%1000==0:
        print(numPrime/numDiag)


print(sideLen+1)