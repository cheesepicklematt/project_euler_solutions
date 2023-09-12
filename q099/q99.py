import os

def expBySquare(b, e):
    """
    Calculates x raised to the power of n using the iterative squaring method.

    Args:
    b: The base.
    e: The exponent.

    Returns:
    x raised to the power of n.
    """
    if e == 0:
        return 1
    y = 1
    while e > 1:
        if e % 2 == 1:
            y *= b
        b *= b
        e //= 2
    return b * y


baseExp = open(os.path.join('q099','0099_base_exp.txt')).read()
baseExp = [[int(y) for y in x.split(',')] for x in baseExp.split('\n')]


valList = []
for b,e in baseExp:
    valList.append(expBySquare(b,e))
    print(b)


