import re
from collections import Counter

s = 'geek55of55gee4ksabc3dr2x'

# Extract digit sequences
a = re.findall(r'\d+', s)

# Count frequencies
freq = Counter(a)

# Track max frequency and number
mx, res = 0, 0

for x in freq:
    if freq[x] >= mx:
        mx = freq[x]          # update max frequency
        res = int(x)          # update result with larger num in tie

print(res)