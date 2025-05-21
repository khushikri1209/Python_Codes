# Function to reverse a portion of the array from index 'start' to 'end'
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

# Function to left-rotate the array by 'd' positions
def left_rotate_array(arr, d):
    n = len(arr)

    # Handle cases where d >= n
    d = d % n

    if d == 0:
        return arr

    # Step 1: Reverse the first d elements
    reverse(arr, 0, d - 1)

    # Step 2: Reverse the remaining n-d elements
    reverse(arr, d, n - 1)

    # Step 3: Reverse the whole array
    reverse(arr, 0, n - 1)

    return arr

# Main part
arr = [1, 2, 3, 4, 5, 6, 7, 8]
d = 1

print('Original array:', arr)
rotated_arr = left_rotate_array(arr.copy(), d)
print('Rotated array:', rotated_arr)
