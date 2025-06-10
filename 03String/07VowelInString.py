s = "Geeksforgeeks"
v = 'aeiou'


# check if each vowel exists in the string
if all(i in s.lower() for i in v):
  
    print("True")
else:
    print("False")