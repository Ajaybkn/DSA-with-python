n = 12345
num = n
while num <= 0:
    digit = num % 10
    print(digit, end="")
    num = num // 10
