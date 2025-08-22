def k_rotations(arr, k):

    n = len(arr)
    rotated = [0] * n
    for i in range(n):
        rotated[(i + k) % n] = arr[i]
    return rotated


ans = k_rotations([1, 2, 3, 4, 5, 6], 8)
print(ans)
