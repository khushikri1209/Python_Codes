# Python3 code to demonstrate working of
# Extract Unique values dictionary values
# Using chain() + sorted() + values()
from itertools import chain

# initializing dictionary
test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Extract Unique values dictionary values
# Using chain() + sorted() + values()
res = list(sorted(set(chain(*test_dict.values()))))

# printing result
print("The unique values list is : " + str(res))