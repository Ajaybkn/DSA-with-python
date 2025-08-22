def find_second_largest(arr):
    largest = arr[0]
    second_largest = float('-inf')
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    for j in range(0, len(arr)):
        if arr[j] > second_largest and arr[j] < largest:
            second_largest = arr[j]
    return second_largest


ans = find_second_largest([55, 32, 97, 9, 3, 67, 2])
print(ans)
