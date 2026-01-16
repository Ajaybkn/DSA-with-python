def floyd’s_triangle(n):
    num=1
    for i in range(n):
        for j in range(i+1):
            print(num,end=" ")
            num+=1
        print()
    
    


floyd’s_triangle(4)