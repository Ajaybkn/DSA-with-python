def linear_search(arr, target):
    n = len(arr)
    li = []
    for i in range(n):
        if arr[i] == target:
            return i
    return -1


ans = linear_search([1, 2, 2, 3, 4, 2, 5], 5)
print(ans)
