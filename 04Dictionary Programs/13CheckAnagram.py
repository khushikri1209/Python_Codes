def is_anagram_binary(a, b):
    bin_a = bin(a)[2:].zfill(32)
    bin_b = bin(b)[2:].zfill(32)
    count_a = [0, 0]
    count_b = [0, 0]
    for i in range(32):
        if bin_a[i] == '0':
            count_a[0] += 1
        else:
            count_a[1] += 1
        if bin_b[i] == '0':
            count_b[0] += 1
        else:
            count_b[1] += 1
    if count_a == count_b:
        return "Yes"
    else:
        return "No"

a = 8
b = 4  
print( is_anagram_binary(8, 4)) # Output: True