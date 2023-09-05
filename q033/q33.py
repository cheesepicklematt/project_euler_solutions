import math
cancelling = []
for a in range(10,100):
    for b in range(10,100):
        if a==b:
            pass
        else:
            strA = str(a)
            strB = str(b)
            common = list(set(strA).intersection(set(strB)))
            if common==[] or common==['0']:
                pass
            else:
                common = common[0]
                divR = a/b
                replaceA = strA.replace(common,'')
                replaceB = strB.replace(common,'')
                if replaceA in ['','0'] or replaceB in ['','0'] or divR>1:
                    pass
                else:
                    divT = int(replaceA)/int(replaceB)
                    if divR==divT:
                        cancelling.append([a,b])

num = 1
den = 1
for x,y in cancelling:
    num = num*x
    den = den*y

gcd = math.gcd(num,den)
print("product of cancelling factions: ",str(int(num/gcd)),'/',str(int(den/gcd)))
