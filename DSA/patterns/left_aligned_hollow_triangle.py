def left_aligned_hollow_triangle(n):
    for i in range(n):
        # first row
        if i == 0:
            print("*")
        # last row
        elif i == n - 1:
            for j in range(n):
                print("* ", end="")
            print()
        # middle rows
        else:
            print("*", end="")            # first star
            for s in range(i - 1):        # inner spaces
                print(" ", end=" ")
            print("*")                   # last star

left_aligned_hollow_triangle(5)
