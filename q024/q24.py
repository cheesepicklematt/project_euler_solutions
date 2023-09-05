import itertools
perm = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))
print('millionth permutation alphabetical of 0-9: ',''.join([str(x) for x in perm[999_999]]))
