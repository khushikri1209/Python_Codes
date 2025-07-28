from functools import reduce
tup = ([5, 6], [6, 7, 8, 9], [3])

res = tuple(reduce(lambda x, y: x + y, tup))
print(res)