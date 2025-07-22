# Python3 code to demonstrate working of
# Extract digits from Tuple list

# initializing list
test_list = [(15, 3), (3, 9), (1, 10), (99, 2)]

# printing original list
print("The original list is : " + str(test_list))
x=""
# Extract digits from Tuple list
for i in test_list:
    for j in i:
        x+=str(j)
res=list(map(int,set(x)))
# printing result
print("The extracted digits : " + str(res))