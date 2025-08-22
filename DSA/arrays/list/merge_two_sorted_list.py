# DUPLICATES IN THE FINAL LIST ARE NOT ALLOWED

def merge_sorted(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    final = []
    for i in range(n):
        if nums1[i] not in final:
            final.append(nums1[i])
    for i in range(m):
        if nums2[i] not in final:
            final.append(nums2[i])
            final.sort()

    return final


ans = merge_sorted([1, 1, 1, 1, 1, 1], [7, 2, 3, 2, 2, 2, 2])
print(ans)
