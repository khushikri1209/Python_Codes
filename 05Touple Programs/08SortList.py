from operator import itemgetter 

a = [(7, 5), (3, 8), (2, 6)]  

# Sort the list based on the second element 
res = sorted(a, key=itemgetter(1))

print(res)