a = [1, 2, 3] # list
b = (4, 5) # tuple
c = [6, 7] # list to add

# add tuple to list `a`
a.append(b)
print(a)

# add list to tuple `b`
d = (*b, *c)
print(d)