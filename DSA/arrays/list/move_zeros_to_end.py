def move_zeros(nums):
    k = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[k] = nums[k], nums[i]
            k += 1
    return nums


ans = move_zeros([0, 1, 0, 3,0,0, 12])
print(ans)  # Output: [1, 3, 12, 0, 0]
