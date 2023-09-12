import collections
import time

t0 = time.time()

def factors(x):
    # We will store all factors in `result`
    result = []
    i = 1
    # This will loop from 1 to int(sqrt(x))
    while i*i <= x:
        # Check if i divides x without leaving a remainder
        if x % i == 0:
            result.append(i)
            # Handle the case explained in the 4th
            if x//i != i: # In Python, // operator performs integer/floored division
                result.append(x//i)
        i += 1
    # Return the list of factors of x (excluding x)
    result.remove(x)
    return result

cashe = collections.defaultdict(int)
def returnFactorSum(n):
    if n in cashe:
        return cashe[n]
    else:
        ans = sum(factors(n))
        cashe[n] = ans
        return ans



maxFactorSize = 1_000_000
maxChainLen = 30


longestChain = 0
longestChainVal = []
for n in range(220,30_000,2):
    fSum = returnFactorSum(n)

    amiNum = {fSum:fSum}
    itr = 0
    while itr<=maxChainLen:
        fSum = returnFactorSum(fSum)
        if fSum > maxFactorSize or fSum < n//2:
            break
        if fSum == n:
            if len(amiNum) > longestChain:
                amiNum[fSum] = fSum
                longestChain = len(amiNum)
                longestChainVal = amiNum
                break
        amiNum[fSum] = fSum
        itr += 1
    
                    
t1 = time.time()

print("the smallest member of the longest amicable chain with no element exceeding one million:",min([x for x in longestChainVal]))
print("run time(s): ",round(t1-t0,3))
