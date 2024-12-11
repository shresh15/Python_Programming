
n = (int)(input("enter number "))
for i in range(1, n + 1): 
      
    for space in range(1, i):
        print(" ", end="")
        
    for num in range(i, n + 1):
        print(num, end=" ")
    print()  



