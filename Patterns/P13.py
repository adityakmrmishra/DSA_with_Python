'''
Print the below pattern 
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''
n=5
initial=0
for i in range(n):
    for j in range(i+1):
        initial=initial+1
        print(initial,end=' ')
    print()