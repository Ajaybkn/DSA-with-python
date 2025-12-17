def isPalindrome(n):
    num = n
    result = 0

    while num > 0:
        ld = num % 10
        num = num // 10
        result = (result * 10) + ld

    if result == n:
        return "Palindrome"
    else:
        return "Not Palindrome"


print(isPalindrome(13))
print(isPalindrome(121))
