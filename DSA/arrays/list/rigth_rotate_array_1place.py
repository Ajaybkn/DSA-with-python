def rotate(arr):
    n = len(arr)
    arr[:] = [arr[n-1]] + arr[0:n-1]
    return arr


ans = rotate([1, 2, 3, 4, 5])
print(ans)  # [5, 1, 2, 3, 4]
