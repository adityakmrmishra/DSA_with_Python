'''
Print the below pattern

*          *
**        **
***      ***
****    ****
*****  *****
************
*****  *****
****    ****
***      ***
**        **
*          *

'''

n=6
# for upper pattern
for i in range(n):    
    for j in range(i+1):
        print("*",end='')
    for j in range(2*n-(2*i+1)-1):
        print(" ",end='')
    for j in range(i+1):
        print("*",end='')    
    print()

# for below pattern
for i in range(n-1):
    for j in range(n-i-1):
        print("*",end='')
    for j in range(2*i+2):
        print(" ",end='')
    for j in range(n-i-1):
        print("*",end='')  
    print()     