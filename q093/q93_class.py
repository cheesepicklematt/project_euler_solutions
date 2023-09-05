import itertools

class q93:
    def __init__(self):
        self.operators = ['+', '-', '*', '/']
        self.maxNum = 10

    def is_integer(self,num):
        if isinstance(num, int):
            return True
        elif isinstance(num, float):
            return num.is_integer()
        else:
            return False

    def evalExprs(self,exprs):
        try:
            return eval(exprs)
        except ZeroDivisionError:
            return -99

    def run(self):
        mostConsecutive = 0
        for self.numList in self.getNumLists():
            groups = self.genListGroupings()
            allExprs = self.genAllExprs(groups)
            results = [self.evalExprs(x) for x in allExprs]
            results = list(set([int(x) for x in results if x>0 and self.is_integer(x)]))

            consecutiveNum = self.getConsecutive(results)
            if consecutiveNum >  mostConsecutive:
                ans = self.numList
                mostConsecutive = consecutiveNum

            print(mostConsecutive,consecutiveNum)


        print("set of four distinct digits, a<b<c<d, for which the longest set of consecutive positive integers, 1 to n is made:",''.join([str(x) for x in ans]))

    def getNumLists(self):
        numLists = []
        for n1 in range(1,self.maxNum):
            for n2 in range(n1+1,self.maxNum):
                for n3 in range(n2+1,self.maxNum):
                    for n4 in range(n3+1,self.maxNum):
                        numLists.append(sorted([n1,n2,n3,n4]))
        return numLists

    def genGroupIdx(self,listLen = 4):
        groupTypes = []
        groupS = [[x for y in range(listLen//x)] for x in range(1,listLen)]
        groupS = [y for x in groupS for y in x]
        for c in range(max(groupS)+1):
            for seq in itertools.combinations(groupS,c):
                if sum(seq) == listLen:
                    groupTypes.append(seq)

        groupTypes = list(set(groupTypes))
        return [[0]+[sum(x[:i + 1]) for i in range(len(x))] for x in groupTypes]

    def genListGroupings(self):
        groupIdx = self.genGroupIdx()
        groups = []
        for perm in itertools.permutations(self.numList):
            for idx in groupIdx:
                groups.append([perm[idx[x-1]:idx[x]] for x in range(1,len(idx))])
        return groups


    def applyOperatorsToList(self,lst):
        exprs = []
        for numL in list(itertools.permutations(lst)):
            for oper in list(itertools.product(self.operators, repeat=len(lst) - 1)):
                exprs.append('('+''.join([str(x)+y for x,y in zip(numL,oper)])+str(numL[-1])+')')
        return exprs

    def genAllExprs(self,groups):
        allExprs = []
        for g in groups:
            subCombo = [self.applyOperatorsToList(x) for x in g]
            if len(subCombo) == 2:
                for s in list(itertools.product(subCombo[0],subCombo[1])):
                    allExprs.append(self.applyOperatorsToList(s))
            else:
                for s in list(itertools.product(subCombo[0],subCombo[1],subCombo[2])):
                    allExprs.append(self.applyOperatorsToList(s))


        allExprs.append(self.applyOperatorsToList(self.numList))

        allExprs = [y for x in allExprs for y in x]
        return list(set(allExprs))

    def getConsecutive(self,results):
        count = 0
        for i in range(1,len(results)+1):
            if i in results:
                count += 1
            else:
                break
        return count

if __name__ == "__main__":
    a = q93()
    a.run()