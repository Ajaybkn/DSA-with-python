def right_triangle(n):
    
    for i in range(n):
        for j in range(i+1):
            print('*',end=" ")
        print()


right_triangle(4)