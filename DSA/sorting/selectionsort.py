

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


final_arr = selection_sort([4, 1, 5, 8, 2, 6, 3, 7])
print(final_arr)
