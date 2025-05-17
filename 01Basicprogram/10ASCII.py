c = 'g'
# print the ASCII value of assigned character in c
print("The ASCII value of '" + c + "' is", ord(c))

print("Enter a String: ", end="")
text = input()
textlength = len(text)
for char in text:
	ascii = ord(char)
	print(char, "\t", ascii)