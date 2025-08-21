# It has adjacent swaps
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


final_arr = bubble_sort([4, 1, 5, 8, 2, 6, 3, 7])
print(final_arr)
