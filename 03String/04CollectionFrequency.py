from collections import Counter

# Input string
s = "hello world hello everyone"

# Calculate word frequencies using Counter
w_freq = Counter(s.split())

print(w_freq)