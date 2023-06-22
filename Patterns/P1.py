'''
Print the below square pattern 
    ***** 
    ***** 
    ***** 
    ***** 
    ***** 

'''

side =int(input("Enter the side of the square "))
for i in range(side):
    for j in range(side):
        print(" * ", end="")

    print("\n")    