'''

print the below pattern
     *
     **
     *** 
     ****
     *****
     ******  
     *****
     ****
     ***    
     **
     *
'''
N=6
for i in range(N):
    for j in range(N):
        if i < j:
            print("",end='')
        else:
            print("*",end='') 
    print()           

for i in range(N-1):    
    for j in range(N-1):
        if i > j:
            print("",end='')
        else:
            print("*",end='') 
    print()