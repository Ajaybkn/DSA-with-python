def inverted_right_triangle(n):
    for i in range(n-1,-1,-1):
        for j in range(i+1):
            print('*',end=" ")
        print()
    
    


inverted_right_triangle(4)