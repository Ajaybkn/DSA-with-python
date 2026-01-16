def pyramid(n):
    for i in range(n):
        # print spaces
        for s in range(n - i - 1):
            print(" ", end="")
        
        # print stars
        for j in range(i + 1):
            print("* ", end="")
        
        # move to next line
        print()

pyramid(4)
