dict = {} # initialize empty dictionary

a = ['bat', 'nat', 'tan', 'ate', 'eat', 'tea']

# Iterate through each word
for word in a:
    sort_word = ''.join(sorted(word))

    if sort_word in dict:
        dict[sort_word].append(word)
    else:
        dict[sort_word] = [word]

res = list(dict.values())
print(res)