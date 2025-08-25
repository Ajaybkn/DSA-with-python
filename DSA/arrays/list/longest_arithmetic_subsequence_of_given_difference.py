# Input: arr = [1, 5, 3, 4, 2], k = 2
# Expected Output: 4 (one valid subsequence is [1, 3, 4, 2])

def longest_subsequence(arr, k):
    # If the array is empty, there is no subsequence
    n = len(arr)
    if n == 0:
        return 0

    # 'best' will track the longest valid subsequence length found so far
    best = 1

    # Try starting a subsequence at every index i
    for i in range(n):
        # Start a new subsequence at position i
        # 'last' is the last chosen element in the current subsequence
        last = arr[i]
        length = 1

        #  scanning forward
        for j in range(i + 1, n):
            # If the next element differs from the last chosen by at most k,
            # we  append it to our subsequence and advance 'last'
            if (arr[j] - last) <= k:
                length += 1
                last = arr[j]

        # After finishing  update the  best
        if length > best:
            best = length

    # Return the longest length
    return best


# Test Cases -->>
ans = longest_subsequence([1, 5, 3, 4, 2], 2)
print(ans)  # 4

ans1 = longest_subsequence([1, 2, 3, 4], 1)
print(ans1)  # 4


ans2 = longest_subsequence([1, 3, 5, 7], 1)
print(ans2)  # 1

ans3 = longest_subsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2)
print(ans3)  # 4
