import os
import string

words = open(os.path.join('euler','q42','0042_words.txt')).read()
words = words.replace('"','').split(',')



alphaDict = {x:i+1 for i,x in enumerate(string.ascii_uppercase)}
triangleVals = [int(0.5*(n*(n+1))) for n in range(1,30)]

tWords = 0
for w in words:
    tmpSum = sum([alphaDict[x] for x in w])
    if tmpSum in triangleVals:
        tWords += 1

print("num triangle words: ",tWords)