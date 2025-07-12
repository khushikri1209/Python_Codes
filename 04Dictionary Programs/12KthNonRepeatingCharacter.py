from collections import OrderedDict

s = "geeksforgeeks"
k = 3

# Count frequency of each character using OrderedDict
freq = OrderedDict()
for char in s:
    freq[char] = freq.get(char, 0) + 1

# Use list comprehension to filter non-repeating characters
a = [char for char, count in freq.items() if count == 1]

# Return the K'th non-repeating character
if k <= len(a):
    print(a[k - 1]) 
else:
    print(None)