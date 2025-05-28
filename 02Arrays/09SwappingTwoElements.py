a = [10, 20, 30, 40, 50]

# Using a temporary variable
# to swap elements at index 2 and 4
temp = a[2]
a[2] = a[4]
a[4] = temp

print(a)