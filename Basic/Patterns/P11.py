'''
print the below pattern

1
01
101
0101
10101
010101

'''

N=6

for i in range(N):
    if i%2 == 0:
        initial=1
    else:
        initial=0
    for j in range(i+1):
        print(initial,end='')
        initial=1-initial
    print()        