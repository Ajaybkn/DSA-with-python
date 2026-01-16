def same_number_in_row(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1,end=" ")
        print()
    
    


same_number_in_row(4)