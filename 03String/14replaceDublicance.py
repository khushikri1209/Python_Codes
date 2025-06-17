# Python3 code to demonstrate working of 
# Replace duplicate Occurrence in String 
# Using split() + enumerate() + loop 

# Initializing string 
test_str = """Gfg is best. Gfg also has Classes now. 
Classes help understand better."""

# Printing original string 
print("The original string is : " + str(test_str)) 

# Initializing replace mapping 
repl_dict = {'Gfg': 'It', 'Classes': 'They'} 

# Replace duplicate Occurrence in String 
# Using split() + enumerate() + loop 
test_list = test_str.split(' ') 
seen = set() 

for idx, word in enumerate(test_list):
    clean_word = word.strip(".")  # Remove punctuation for clean comparison
    if clean_word in repl_dict:
        if clean_word in seen:
            # Preserve punctuation if present
            test_list[idx] = repl_dict[clean_word] + ('.' if word.endswith('.') else '')
        else:
            seen.add(clean_word)

# Joining back to string
result = ' '.join(test_list)

# Printing result 
print("The string after replacing : " + result)
