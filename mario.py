def print_square(size):
    
    #For each brick in square
    for i in range(size):
        #for each brick in row
        for j in range(size):
            
            print("#", end = "")
        print()
    
size = int(input("What's the size of the square? "))

print_square(size)