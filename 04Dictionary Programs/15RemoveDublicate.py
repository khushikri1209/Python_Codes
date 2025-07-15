s1 = "Geeks for Geeks"
a = s1.split()  # Split the sentence into words
seen = set()  # Set to track unique words

# Use list comprehension to filter out duplicates while maintaining order
res = [word for word in a if not (word in seen or seen.add(word))]

# Join the list back into a sentence
s2 = ' '.join(res)
print(s2)