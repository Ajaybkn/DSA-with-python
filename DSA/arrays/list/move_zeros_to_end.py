def move_zeros(nums):
    n = len(nums)
    for i in range(n):
        if nums[i] == 0:
            if (nums[n-1] != 0):
                nums[i], nums[n-1] = nums[i], nums[n-1]

    return nums


ans = move_zeros([0, 1, 0, 3, 12])
print(ans)  # Output: [1, 3, 12, 0, 0]
