import math
import time

t0 = time.time()

limit = 12000
maxSolution = 2*limit
maxIter = 12000

fillNum = 999_999_999
solDict = {k:fillNum for k in range(2,limit*2)}

lst = []
for n1 in range(1,maxIter):
    for n2 in range(n1,maxIter):
        if n1*n2> maxSolution:
            break
        for n3 in range(n2,maxIter):
            if n1*n2*n3> maxSolution:
                break
            for n4 in range(n3,maxIter):
                if n1*n2*n3*n4> maxSolution:
                    break
                for n5 in range(n4,maxIter):
                    if n1*n2*n3*n4*n5> maxSolution:
                        break
                    for n6 in range(n5,maxIter):
                        if n1*n2*n3*n4*n5*n6> maxSolution:
                            break
                        for n7 in range(n6,maxIter):
                            if n1*n2*n3*n4*n5*n6*n7> maxSolution:
                                break   
                            for n8 in range(n7,maxIter):
                                if n1*n2*n3*n4*n5*n6*n7*n8> maxSolution:
                                    break
                                for n9 in range(n8,maxIter):
                                    if n1*n2*n3*n4*n5*n6*n7*n8*n9> maxSolution:
                                        break
                                    for n10 in range(n9,maxIter):
                                        if n1*n2*n3*n4*n5*n6*n7*n8*n9*n10> maxSolution:
                                            break
                                        for n11 in range(n10,maxIter):
                                            if n1*n2*n3*n4*n5*n6*n7*n8*n9*n10*n11> maxSolution:
                                                break
                                            for n12 in range(n11,maxIter):
                                                if n1*n2*n3*n4*n5*n6*n7*n8*n9*n10*n11*n12> maxSolution:
                                                    break
                                                for n13 in range(n12,maxIter):
                                                    if n1*n2*n3*n4*n5*n6*n7*n8*n9*n10*n11*n12*n13> maxSolution:
                                                        break

                                                    tmpLst = [x for x in [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13] if x!=1]
                                                    if tmpLst!=[] and len(tmpLst)!=1:
                                                        tmpProd = math.prod(tmpLst)
                                                        tmpSum = sum(tmpLst)
                                                        tmpOnes = tmpProd - tmpSum
                                                        k = tmpOnes + len(tmpLst)

                                                        tmpSol = solDict[k]
                                                        if tmpProd<tmpSol:
                                                            solDict[k] = tmpProd


t = set([solDict[x] for x in solDict if x<=limit and solDict[x]!=fillNum])
t1 = time.time()


print("sum of all the minimal product-sum numbers for 2 <= k <= 12000: ",sum(t))
print("run time(s): ",round(t1-t0,3))