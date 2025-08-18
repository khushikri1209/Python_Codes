# python code to find most occurring character in a string and its count
string1="geeksforgeeks"
list1=[]
list2=[]
for i in string1:
  if i not in list1:
    list1.append(i)#appending unique characters of string
    list2.append(string1.count(i))
#finding maximum in the list
occ=max(list2)
ele=list1[list2.index(occ)]
print(ele,occ)