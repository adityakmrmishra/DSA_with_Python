'''
Print the below  pattern 
***********
 *********
  *******
   ***** 
    ***    
     *

'''


# N = int(input("Enter the size:"))

N=6

for i in range(N):
    for j in range(0,i):
        print(" ",end='')
    for k in range(0,2*N-(2*i+1)):
        print("*",end='')    
    for j in range(0,i):
        print(" ",end='')
    print()    
