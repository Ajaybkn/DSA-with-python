def is_sorted(arr):
    if len(arr) < 2:
        return True
    for x in range(0, len(arr)-1):
        if arr[x] > arr[x+1]:
            return False
    return True


ans = is_sorted([1, 2, 5, 4, 5])
print(ans)
