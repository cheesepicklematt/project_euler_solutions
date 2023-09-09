import numpy as np
import collections


def get_all_integer_points_on_line(x1, y1, x2, y2):
    points = []

    # Calculate differences between endpoints
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Determine the sign of the slope
    if x1 < x2:
        sx = 1
    else:
        sx = -1
    if y1 < y2:
        sy = 1
    else:
        sy = -1

    # Initialize error term
    err = dx - dy

    # Initial coordinates
    x = x1
    y = y1

    while True:
        # Add the current point to the list
        points.append((x, y))

        # Check if we've reached the end point
        if x == x2 and y == y2:
            break

        # Calculate the next x or y coordinate
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy

    return points

def getY(g,qy,qx):
    xVal = [0,50]
    return [z for z in [[g*x - g*qx + qy,x] for x in xVal] if z[0]>=xVal[0] and z[0]<=xVal[1]]

def getX(g,qy,qx):
    yVal = [0,50]
    return [z for z in [[y,(y + g*qx - qy)/g] for y in yVal] if z[1]>=yVal[0] and z[1]<=yVal[1]]





maxLen = 50
loopMax = maxLen + 1

origin = np.array([0,0])

cooDict = collections.defaultdict(set)



for qy in range(1,loopMax):
    for qx in range(0,loopMax):
        if qy == 0:
            for y in range(1,loopMax):
                if (qy,qx)!=(y,qx):
                    cooDict['co'].add(tuple([(0,0),(qy,qx),(y,qx)]))
        if qx == 0:
            for x in range(1,loopMax):
                if (qy,qx)!=(qy,x):
                    cooDict['co'].add(tuple([(0,0),(qy,qx),(qy,x)]))
        else:
            g = -1/(qy/qx)
            intercept = getY(g,qy,qx) + getX(g,qy,qx)
            for a,b in intercept:
                for z in get_all_integer_points_on_line(x1=qx, y1=qy, x2=b, y2=a):
                    if (qy,qx)!=(z):
                        cooDict['co'].add(tuple([(0,0),(qy,qx),(z)]))
    print(qy)

len(cooDict['co'])
        
