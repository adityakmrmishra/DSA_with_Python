'''
Print the below pattern

************
*****  *****
****    ****
***      ***     
**        **
*          *     upper end
*          *     lower start
**        **
***      ***
****    ****
*****  *****
************

'''
n=6
# for upper pattern
for i in range(n):
    for j in range(n-i):
        print("*",end='')
    for j in range(2*i):
        print(" ",end='')
    for j in range(n-i):
        print("*",end='')  
    print() 
# for below pattern    
for i in range(n):    
    for j in range(i+1):
        print("*",end='')
    for j in range(2*n-(2*i+1)-1):
        print(" ",end='')
    for j in range(i+1):
        print("*",end='')    
    print()