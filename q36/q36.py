
palNumSum = 0
for n in range(1_000_000):
    nStr = str(n)
    nRev = nStr[::-1]
    nBin = bin(n)[2:]
    nBinRev = nBin[::-1]
    if nStr==nRev and nBin==nBinRev:
        palNumSum += n




