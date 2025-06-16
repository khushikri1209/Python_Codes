import re

s = "101010000111"

# check if string matches binary pattern
if re.fullmatch('[01]+', s):
    print("Yes")
else:
    print("No")