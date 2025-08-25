def missing_number(nums):
    n = len(nums)
    while n >= 0:
        if n not in nums:
            return n
        n -= 1
    return -1


print(missing_number([0, 1]))
