from collections import Counter
s = "GeeksforGeeks"
freq = Counter(s)
res = min(freq, key=freq.get)
print(str(res))