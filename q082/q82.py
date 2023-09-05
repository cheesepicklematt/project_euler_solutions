import numpy as np
import os
import time

def prepareData():
    '''
    import data and clean from raw text format
    prepare mask (cost) which will house all the shortest paths
    '''
    matrix = open(os.path.join('euler','q82','0082_matrix.txt')).read()
    matrix = [[int(y) for y in x.split(',')] for x in matrix.split('\n') if x!='']
    rows, cols = len(matrix), len(matrix[0])

    # prepare array
    cost = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        cost[i][0] = matrix[i][0]
    matrix = np.array(matrix)
    cost = np.array(cost)

    return matrix, cost, rows, cols

def findLocalShortest(y,x):
    '''
    find the shortest path to current cell (y,x) from the previous column
    '''
    pathLen = []
    for i in range(y+1,rows+1):
        pathLen.append(cost[i-1][x-1]+sum(matrix[y+1:i,x]))
    for i in range(y-1,-1,-1):
        pathLen.append(cost[i][x-1]+sum(matrix[i:y,x]))
    return min(pathLen)


t0 = time.time()

matrix, cost, rows, cols = prepareData()
for x in range(1,cols):
    for y in range(rows):
        cost[y][x] = matrix[y][x] + findLocalShortest(y,x)

t1 = time.time()

print("shortest path: ",min(cost[:,-1]))
print("time taken: ",t1 - t0," sec")