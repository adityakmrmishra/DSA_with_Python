'''
Print the below pattern 
1          1
12        21
12       321
1234    4321
12345  54321
123456654321

'''
n=6
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')   
    for j in range(1,2*n-(2*i-1)):
        print(" ",end='')
    for j in range(i,0,-1):
        print(j,end='')      
    print()   
