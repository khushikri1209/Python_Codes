from collections import OrderedDict

s = "geeksforgeeks"
res = "".join(OrderedDict.fromkeys(s))
print(res)