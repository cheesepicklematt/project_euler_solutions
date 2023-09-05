import os
import string

names = open(os.path.join('euler','q22','0022_names.txt')).read()
names = names.replace('"','').split(',')
names.sort()

alphaDict = {x:i+1 for i,x in enumerate(string.ascii_uppercase)}
totalScore = 0
for i,n in enumerate(names):
    totalScore += (i+1)*sum([alphaDict[x] for x in n])


print('total score: ',totalScore)
