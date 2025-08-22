def remove_duplicates(arr):
    dictn = {}
    for i in range(0, len(arr)):
        dictn[arr[i]] = 0
    j = 0
    for k in dictn:
        arr[j] = k
        j += 1
    return arr[:j]


ans = remove_duplicates([1, 1, 1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 6])
print(ans)

#  2nd Method--->>>


def remove_duplicates(arr):
    ans = []
    for i in arr:
        if i not in ans:
            ans.append(i)
    return ans


answ = remove_duplicates([1, 1, 1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 6])
print(answ)
