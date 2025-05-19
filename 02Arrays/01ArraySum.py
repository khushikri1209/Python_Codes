def _sum(arr):
    total = 0
    for i in arr:
        total += i
    return total

arr = [12, 3, 4, 15]
print('Sum of the array is', _sum(arr))
