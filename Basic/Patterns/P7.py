'''
Print the below  pattern 
     *     
    ***    
   *****   
  *******  
 ********* 
***********

'''

N = int(input("Enter the size:"))
for i in range(N):
    for j in range(0,N-i-1):
        print(" ", end='')
    for k in range(0,2*i+1):
        print("*", end='')        
    for j in range(0,N-i-1):
        print(" ", end='')    
    print()    