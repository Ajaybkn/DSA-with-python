def find_largest(arr):
    largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest


ans = find_largest([-55, -32, -97, -99, -3, -67, -2])
print(ans)
